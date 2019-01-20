# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T17:59:13+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: moka_payment.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T19:31:26+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from moka.moka_checkout import set_redirect

class MokaPayment(Document):
	def on_update(self):
		set_redirect(self)
