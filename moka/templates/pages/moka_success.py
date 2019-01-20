# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T18:00:40+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: moka_success.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T21:12:47+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from __future__ import unicode_literals

import frappe

def get_context(context):
	token = frappe.local.form_dict.token
