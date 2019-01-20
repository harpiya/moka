/**
 * @Author: Saadettin Yasir AKEL <developer>
 * @Date:   2019-01-20T17:58:24+03:00
 * @Email:  yasir@harpiya.com
 * @Project: Harpiya Kurumsal Yönetim Sistemi
 * @Filename: moka_settings.js
 * @Last modified by:   developer
 * @Last modified time: 2019-01-20T19:29:42+03:00
 * @License: MIT License. See license.txt
 * @Copyright: Harpiya Yazılım Teknolojileri
 */



frappe.ui.form.on("Moka Settings", {
	refresh: function(frm) {
		frm.add_custom_button(__("Moka Logs"), function() {
			frappe.set_route("List", "Moka Log");
		})
		frm.add_custom_button(__("Payment Logs"), function() {
			frappe.set_route("List", "Moka Payment");
		});
		frm.add_custom_button(__("Payment Gateway Accounts"), function() {
			frappe.route_options = {"payment_gateway": "Moka"};
			frappe.set_route("List", "Payment Gateway Account");
		});
	}
})
