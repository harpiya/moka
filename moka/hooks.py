# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-18T21:16:35+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: hooks.py
# @Last modified by:   developer
# @Last modified time: 2019-01-19T01:33:38+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "moka"
app_title = "Moka"
app_publisher = "Harpiya Yazılım Teknolojileri."
app_description = "Moka Ödeme Sistemi"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@harpiya.com"
app_license = "MIT"


integration_services = ["Moka"]
app_include_js = "/assets/js/moka_settings.js"

website_route_rules = [
	{ "from_route": "/integrations/moka_checkout/<name>", "to_route": "integrations/moka_checkout" }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/moka/css/moka.css"
# app_include_js = "/assets/moka/js/moka.js"

# include js, css files in header of web template
# web_include_css = "/assets/moka/css/moka.css"
# web_include_js = "/assets/moka/js/moka.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "moka.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "moka.install.before_install"
# after_install = "moka.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "moka.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"moka.tasks.all"
# 	],
# 	"daily": [
# 		"moka.tasks.daily"
# 	],
# 	"hourly": [
# 		"moka.tasks.hourly"
# 	],
# 	"weekly": [
# 		"moka.tasks.weekly"
# 	]
# 	"monthly": [
# 		"moka.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "moka.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "moka.event.get_events"
# }
