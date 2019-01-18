# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-18T21:16:35+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: utils.py
# @Last modified by:   developer
# @Last modified time: 2019-01-18T21:32:40+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from __future__ import unicode_literals
import frappe
from frappe import _, session

def _range(a,b):
	return [x for x in range(a,b)]

CARDS = {
	'AMEX':         [34, 37],
	'CHINAUP':      [62, 88],
	'DinersClub':   _range(300, 305)+[309, 36, 54, 55]+_range(38, 39),
	'DISCOVER':     [6011, 65] + _range(622126, 622925) + _range(644, 649),
	'JCB':          _range(3528, 3589),
	'LASER':        [6304, 6706, 6771, 6709],
	'MAESTRO':      [5018, 5020, 5038, 5612, 5893, 6304, 6759, 6761, 6762, 6763, 0604, 6390],
	'DANKORT':      [5019],
	'MASTERCARD':   _range(50, 55),
	'VISA':         [4],
	'VISAELECTRON': [4026, 417500, 4405, 4508, 4844, 4913, 4917]
}

def get_contact(contact_name = None):
	user = session.user
	contact = None
	if isinstance(user, unicode):
		user = frappe.get_doc("User", user)

	if not contact_name:
		contact_names = frappe.get_all("Contact", fields=["name"], filters={
			"user": user.name
		})

		if not contact_names or len(contact_names) == 0:
			contact_names = frappe.get_all("Contact", fields=["name"], filters={
				"email_id": user.email
			})

		if contact_names and len(contact_names) > 0:
			contact_name = contact_names[0].get("name")

	if contact_name:
		contact = frappe.get_doc("Contact", contact_name)

	return contact


def get_card_accronym(number):
	card_name = ''
	card_match_size = 0
	for name, values in CARDS.items():
		for digits in values:
			digits = str(digits)
			if number.startswith(digits):
				if len(digits) > card_match_size:
					card_match_size = len(digits)
					card_name = name

	return card_name

def moka_address(fields):
	address = {}
	if fields is None:
		return address
	if fields.get("address_1"):
		address["address"] = "%s %s %s/%s" % (fields.get("address_1"), fields.get("address_2", ""), fields.get("city"), fields.get('state'))
		address["address"] = address["address"][:60]
	return address
