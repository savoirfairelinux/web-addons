/*
    © 2018 Savoir-faire Linux <https://savoirfairelinux.com>
    License LGPL-3.0 or later (http://www.gnu.org/licenses/LGPL.html).
*/

odoo.define('web_calendar_custom.renderer_setting', function (require) {
"use strict";

    /* Dirty hack to get FullCalendar settings from settings model under project_resource_calendar project-addons*/
    var testValue = '';
    rpc.query({
              model: 'setting',
              method: 'get_settings',
              args: []
    //}).then(function (returned_value) { testValue = returned_value;});
    }).then(function (returned_value) { alert("Toto");});

    //web.CalendarRenderer._initCalendar.include({

        /*Override the original _initCalendar for the fullCalendar*/

      //   minTime: '07:00',


    //});


});


/*
    var core = require('web.core');
    var rpc = require('web.rpc');
    var form_widgets = require('web.form_widgets');
    var _t = core._t;

    form_widgets.FieldFloat.include({
        set_value: function(value_) {

            if (this.options.no_default_value === 1){
                var placeholder = '0';
                var precision = this.digits[1];
                if (precision != 0){
                    placeholder += _t.database.parameters.decimal_point;
                    placeholder += '0'.repeat(precision);
                }
                this.node.attrs.placeholder = placeholder;
                this.set({'value': value_});
            } else {
                this._super(value_);
            }
        }
    });
*/