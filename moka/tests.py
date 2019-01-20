# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T17:55:20+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: tests.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T18:33:16+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from unittest import TestCase

from . import moka_checkout
import frappe

class TestMokaCheckout(TestCase):
	def test_set_moka_checkout(self):
		moka_checkout.set_moka_checkout(100, "USD")
		self.assertEquals(frappe.local.response["type"], "redirect")
