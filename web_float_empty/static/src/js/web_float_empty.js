/*
    © 2018 Savoir-faire Linux <https://savoirfairelinux.com>
    License LGPL-3.0 or later (http://www.gnu.org/licenses/LGPL.html).
*/
odoo.define('web_float_empty', function(require) {
    "use strict";

    var form_widgets = require('web.form_widgets');

    form_widgets.FieldFloat.include({
        set_value: function(value_) {
            /*
                Override the original function to avoid setting
                a default value 0 on floats that have the option 
                no_default_value set to 1.
            */
            if (this.options.no_default_value === 1){
                this.node.attrs.placeholder = '0,00';
                this.set({'value': value_});
            } else {
                this._super(value_);
            }
        }
    });
});
