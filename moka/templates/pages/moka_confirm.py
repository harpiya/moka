# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T18:00:21+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: moka_confirm.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T21:12:30+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri

from __future__ import unicode_literals

import frappe, json

no_cache = True

def get_context(context):
	token = frappe.local.form_dict.token

	if token:
		moka_payment = frappe.get_doc("Moka Payment", token)
		moka_payment.status = "Verified"
		moka_payment.save(ignore_permissions=True)
		frappe.db.commit()

	context.token = token
	context.data = json.loads(moka_payment.data or "{}")
