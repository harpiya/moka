/**
 * @Author: Saadettin Yasir AKEL <developer>
 * @Date:   2019-01-18T21:20:01+03:00
 * @Email:  yasir@harpiya.com
 * @Project: Harpiya Kurumsal Yönetim Sistemi
 * @Filename: moka_settings.js
 * @Last modified by:   developer
 * @Last modified time: 2019-01-18T23:54:00+03:00
 * @License: MIT License. See license.txt
 * @Copyright: Harpiya Yazılım Teknolojileri
 */



frappe.provide("frappe.integration_service")

frappe.ui.form.on('Moka Settings', {
	refresh: function(frm) {

	}
});

frappe.integration_service.moka_settings =  Class.extend({
	init: function(frm) {

	},

	get_scheduler_job_info: function() {
		return  {}
	},

	get_service_info: function(frm) {
		frappe.call({
			method: "moka.moka.doctype.moka_settings.moka_settings.get_service_details",
			callback: function(r) {
				var integration_service_help = frm.fields_dict.integration_service_help.wrapper;
				$(integration_service_help).empty();
				$(integration_service_help).append(r.message);
			}
		})
	}
})
