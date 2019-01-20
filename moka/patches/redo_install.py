# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T21:28:46+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: redo_install.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T21:37:29+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



import frappe

def execute():
	# should create payment gateway and payment gateway account
	try:
		frappe.get_doc("Moka Settings").save()
	except frappe.MandatoryError:
		pass
