/**
 * @Author: Saadettin Yasir AKEL <developer>
 * @Date:   2019-01-18T21:16:35+03:00
 * @Email:  yasir@harpiya.com
 * @Project: Harpiya Kurumsal Yönetim Sistemi
 * @Filename: form.js
 * @Last modified by:   developer
 * @Last modified time: 2019-01-19T01:28:18+03:00
 * @License: MIT License. See license.txt
 * @Copyright: Harpiya Yazılım Teknolojileri
 */



frappe.provide("frappe.integration_service")

{% include "templates/includes/integrations/moka/process.js" with context %}

frappe.integration_service.moka_gateway =  frappe.integration_service.moka_gateway.extend({
  form: function(reference_id, display_errors) {
    this._super();
    var base = this;
    $(function() {
      // trigger processing info
      $('#authorizenet-process-btn').click(function() {
        var billing_info = base.collect_billing_info();
        var card_info = base.collect_card_info();
        var stored_payment_options = base.collect_stored_payment_info();

        $('#authorizenet-payment').fadeOut('fast');
        $('#authorizenet-process-btn').fadeOut('fast');
        base.process_card(card_info, billing_info, stored_payment_options, reference_id,
          function(err, result) {
            if ( err ) {
							if ( display_errors && err.errors ) {
								frappe.msgprint(err.errors.join("\n"));
							}
              $('#authorizenet-error').text(err.error)
              $('#authorizenet-payment').fadeIn('fast');
              $('#authorizenet-process-btn').fadeIn('fast');
            } else {
              window.location.href = result.redirect_to;
            }
          })
      })

    })

  }

});
