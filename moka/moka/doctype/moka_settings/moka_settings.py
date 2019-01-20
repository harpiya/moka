# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T17:58:24+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: moka_settings.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T19:37:19+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from moka.moka_checkout import validate_moka_credentials

class MokaSettings(Document):
	def validate(self):
		if self.get("__islocal"):
			self.validate_moka_credentials()

	def validate_moka_credentials(self):
		validate_moka_credentials(self, "validate_moka_credentials")

	def on_update(self):
		create_payment_gateway_and_account()


def create_payment_gateway_and_account():
	"""If ERPNext is installed, create Payment Gateway and Payment Gateway Account"""
	if "erpnext" not in frappe.get_installed_apps():
		return

	create_payment_gateway()
	create_payment_gateway_account()

def create_payment_gateway():
	# NOTE: we don't translate Payment Gateway name because it is an internal doctype
	if not frappe.db.exists("Payment Gateway", "Moka"):
		payment_gateway = frappe.get_doc({
			"doctype": "Payment Gateway",
			"gateway": "Moka"
		})
		payment_gateway.insert(ignore_permissions=True)

def create_payment_gateway_account():
	from erpnext.setup.setup_wizard.setup_wizard import create_bank_account

	company = frappe.db.get_value("Global Defaults", None, "default_company")
	if not company:
		return

	# NOTE: we translate Payment Gateway account name because that is going to be used by the end user
	bank_account = frappe.db.get_value("Account", {"account_name": _("Moka"), "company": company},
		["name", 'account_currency'], as_dict=1)

	if not bank_account:
		# check for untranslated one
		bank_account = frappe.db.get_value("Account", {"account_name": "Moka", "company": company},
			["name", 'account_currency'], as_dict=1)

	if not bank_account:
		# try creating one
		bank_account = create_bank_account({"company_name": company, "bank_account": _("Moka")})

	if not bank_account:
		frappe.msgprint(_("Payment Gateway Account not created, please create one manually."))
		return

	# if payment gateway account exists, return
	if frappe.db.exists("Payment Gateway Account",
		{"payment_gateway": "Moka", "currency": bank_account.account_currency}):
		return

	try:
		frappe.get_doc({
			"doctype": "Payment Gateway Account",
			"is_default": 1,
			"payment_gateway": "Moka",
			"payment_account": bank_account.name,
			"currency": bank_account.account_currency
		}).insert(ignore_permissions=True)

	except frappe.DuplicateEntryError:
		# already exists, due to a reinstall?
		pass
