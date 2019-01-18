# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-18T21:19:17+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: moka_request.py
# @Last modified by:   developer
# @Last modified time: 2019-01-18T23:55:36+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime

LOG_LEVELS = {
	"None": 0,
	"Info": 1,
	"Error": 2,
	"Debug": 3
}

class MokaRequest(Document):

	def max_log_level(self, level):
		self._max_log_level = LOG_LEVELS[level]

	def log_action(self, data, level):
		if LOG_LEVELS[level] <= self._max_log_level:
			self.append("log",{
				"doctype": "Moka Request Log",
				"log": data,
				"level": level,
				"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			})
