# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-20T17:55:20+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: hooks.py
# @Last modified by:   developer
# @Last modified time: 2019-01-20T19:53:31+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri

from __future__ import unicode_literals

app_name = "moka"
app_title = "Moka"
app_publisher = "Harpiya Yazılım Teknolojileri"
app_description = "Moka Ödeme Sistemi"
app_icon = "octicon octicon-credit-card"
app_color = "#179bd7"
app_email = "info@harpiya.com"
app_version = "0.0.1"
hide_in_installer = True
app_license = "MIT"

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
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Payment Request": {
		"validate": "moka.express_checkout.validate_moka_credentials",
		"get_payment_url": "moka.utils.get_payment_url"
	},
	"Shopping Cart Settings": {
		"validate": "moka.utils.validate_price_list_currency"
	}
}

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
