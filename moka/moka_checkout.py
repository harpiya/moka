# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T18:01:23+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: moka_checkout.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T21:27:55+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri


from __future__ import unicode_literals
import frappe
from frappe.utils import get_url
from urllib import urlencode
import urlparse, json
from frappe import _
from frappe.utils import get_request_session



class MokaException(Exception): pass

def validate_moka_credentials(self):
	pass

@frappe.whitelist(allow_guest=True, xss_safe=True)
def set_moka_checkout(amount, currency="USD", data=None):
	validate_transaction_currency(currency)

	if not isinstance(data, basestring):
		data = frappe.as_json(data or "{}")

	response = execute_set_moka_checkout(amount, currency)

	if not response["success"]:
		moka_log(response)
		frappe.db.commit()

		frappe.respond_as_web_page(_("Something went wrong"),
			_("Looks like something is wrong with this site's Moka configuration. Don't worry! No payment has been made from your Moka account."),
			success=False,
			http_status_code=frappe.ValidationError.http_status_code)

		return

	moka_settings = get_moka_settings()
	if moka_settings.moka_sandbox:
		return_url = "{0}"
	else:
		return_url = "{0}"

	token = response.get("Data")
	moka_payment = frappe.get_doc({
		"doctype": "Moka Payment",
		"status": "Started",
		"amount": amount,
		"currency": currency,
		"token": token,
		"data": data,
		"correlation_id": response.get("CORRELATIONID")[0]
	})
	if data:
		if isinstance(data, basestring):
			data = json.loads(data)

		if data.get("doctype") and data.get("docname"):
			moka_payment.reference_doctype = data.get("doctype")
			moka_payment.reference_docname = data.get("docname")

	moka_payment.insert(ignore_permissions = True)
	frappe.db.commit()

	frappe.local.response["type"] = "redirect"
	frappe.local.response["location"] = return_url.format(token)

def execute_set_moka_checkout(amount, currency):
	params = get_moka_params()
	params.update({
		"METHOD": "SetExpressCheckout",
		"PAYMENTREQUEST_0_PAYMENTACTION": "SALE",
		"PAYMENTREQUEST_0_AMT": amount,
		"PAYMENTREQUEST_0_CURRENCYCODE": currency
	})

	return_url = get_url("/api/method/moka.moka_checkout.get_moka_checkout_details")

	params = urlencode(params) + \
		"&returnUrl={0}&cancelUrl={1}".format(return_url, get_url("/moka-cancel"))

	return get_api_response(params.encode("utf-8"))

@frappe.whitelist(allow_guest=True, xss_safe=True)
def get_moka_checkout_details(token):
	params = get_moka_params()
	params.update({
		"METHOD": "GetExpressCheckoutDetails",
		"TOKEN": token
	})

	response = get_api_response(params)

	if not response["success"]:
		moka_log(response, params)
		frappe.db.commit()

		frappe.respond_as_web_page(_("Something went wrong"),
			_("Looks like something went wrong during the transaction. Since we haven't confirmed the payment, Moka will automatically refund you this amount. If it doesn't, please send us an email and mention the Correlation ID: {0}.").format(response.get("CORRELATIONID", [None])[0]),
			success=False,
			http_status_code=frappe.ValidationError.http_status_code)

		return

	moka_payment = frappe.get_doc("Moka Payment", token)
	moka_payment.payerid = response.get("PAYERID")[0]
	moka_payment.payer_email = response.get("EMAIL")[0]
	moka_payment.status = "Verified"
	moka_payment.save(ignore_permissions=True)
	frappe.db.commit()

	frappe.local.response["type"] = "redirect"
	frappe.local.response["location"] = get_url( \
		"/api/method/moka.moka_checkout.confirm_payment?token="+moka_payment.token)

@frappe.whitelist(allow_guest=True, xss_safe=True)
def confirm_payment(token):
	moka_payment = frappe.get_doc("Moka Payment", token)

	params = get_moka_params()
	params.update({
		"METHOD": "DoExpressCheckoutPayment",
		"PAYERID": moka_payment.payerid,
		"TOKEN": moka_payment.token,
		"PAYMENTREQUEST_0_PAYMENTACTION": "SALE",
		"PAYMENTREQUEST_0_AMT": moka_payment.amount,
		"PAYMENTREQUEST_0_CURRENCYCODE": moka_payment.currency
	})

	response = get_api_response(params)

	if response["success"]:
		moka_payment.status = "Completed"
		moka_payment.transaction_id = response.get("PAYMENTINFO_0_TRANSACTIONID")[0]
		moka_payment.correlation_id = response.get("CORRELATIONID")[0]
		moka_payment.flags.redirect = True
		moka_payment.flags.redirect_to = get_url("/moka-success")
		moka_payment.flags.status_changed_to = "Completed"
		moka_payment.save(ignore_permissions=True)

	else:
		moka_payment.status = "Failed"
		moka_payment.flags.redirect = True
		moka_payment.flags.redirect_to = get_url("/moka-failed")
		moka_payment.save(ignore_permissions=True)

		moka_log(response, params)

	frappe.db.commit()

	# this is done so that functions called via hooks can update flags.redirect_to
	if moka_payment.flags.redirect:
		frappe.local.response["type"] = "redirect"
		frappe.local.response["location"] = moka_payment.flags.redirect_to

def get_moka_params():
	moka_settings = get_moka_settings()
	if moka_settings.api_username:
		return {
			"PaymentDealerAuthentication": {
				"DealerCode": moka_settings.dealer_code,
				"Username": moka_settings.api_username,
				"Password": moka_settings.api_password,
			}
		}

	else :
		return {
			"USER": frappe.conf.moka_username,
			"PWD": frappe.conf.moka_password,
			"SIGNATURE": frappe.conf.moka_signature,
			"VERSION": "98"
		}

def get_api_url(moka_settings=None):
	if not moka_settings:
		moka_settings = get_moka_settings()

	if moka_settings.moka_sandbox:
		return "https://clientwebpos.testmoka.com/Api/WebPos/CreateWebPosRequest"
	else:
		return "https://clientwebpos.moka.com/Api/WebPos/CreateWebPosRequest"

def get_api_response(params, api_url=None):
	s = get_request_session()
	response = s.post(api_url or get_api_url(), data=params)
	response = urlparse.parse_qs(response.text)
	response["success"] = response.get("ResultCode")=="Success"
	return response

def get_moka_settings():
	moka_settings = frappe.get_doc("Moka Settings")

	# update from site_config.json
	for key in ("moka_sandbox", "moka_username", "moka_password", "moka_signature"):
		if key in frappe.local.conf:
			moka_settings.set(key, frappe.local.conf[key])

	return moka_settings

def validate_transaction_currency(currency):
	if currency not in ["AUD", "BRL", "CAD", "CZK", "DKK", "EUR", "HKD", "HUF", "ILS", "JPY", "MYR", "MXN",
		"TWD", "NZD", "NOK", "PHP", "PLN", "GBP", "RUB", "SGD", "SEK", "CHF", "THB", "TRY", "USD"]:
		frappe.throw(_("Please select another payment method. Moka does not support transactions in currency '{0}'").format(currency))

def moka_log(response, params=None):
	frappe.get_doc({
		"doctype": "Moka Log",
		"error": frappe.as_json(response),
		"params": frappe.as_json(params or "")
	}).insert(ignore_permissions=True)

def set_redirect(moka_payment):
	"""HarpiyaERP related redirects.
	   You need to set Moka Payment.flags.redirect_to on status change.
	   Called via MokaPayment.on_update"""

	reference_doctype = moka_payment.reference_doctype
	reference_docname = moka_payment.reference_docname

	if reference_doctype and reference_docname:
		reference_doc = frappe.get_doc(reference_doctype, reference_docname)
		reference_doc.run_method('on_payment_authorized')

	if "erpnext" not in frappe.get_installed_apps():
		return

	if not moka_payment.flags.status_changed_to:
		return


	if not reference_doc:
		return

	shopping_cart_settings = frappe.get_doc("Shopping Cart Settings")

	if moka_payment.flags.status_changed_to == "Completed":
		reference_doc.run_method("set_as_paid")

		# if shopping cart enabled and in session
		if (shopping_cart_settings.enabled
			and hasattr(frappe.local, "session")
			and frappe.local.session.user != "Guest"):

			success_url = shopping_cart_settings.payment_success_url
			if success_url:
				moka_payment.flags.redirect_to = ({
					"Orders": "orders",
					"Invoices": "invoices",
					"My Account": "me"
				}).get(success_url, "me")
			else:
				moka_payment.flags.redirect_to = get_url("/orders/{0}".format(reference_doc.reference_name))

	elif moka_payment.flags.status_changed_to == "Cancelled":
		reference_doc.run_method("set_as_cancelled")
