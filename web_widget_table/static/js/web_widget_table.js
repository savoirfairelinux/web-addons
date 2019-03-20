
odoo.define('web_widget_table', function(require)
{
    var registry = require('web.field_registry'),
        AbstractField = require('web.AbstractField');
    var FieldMany2OneTable = AbstractField.extend({
        className: 'oe_form_field_many2one_buttons',
        supportedFieldTypes: ['many2one','char'],
        
        init: function()
        {
            this._super.apply(this, arguments);
        },
        events: {
            'click .btn': '_button_clicked',
        },
        
        _render: function()
        {
            var self = this;
            var field = this.nodeOptions['field_name'];
            var fieldModel = this.record.data[field].model
            var fieldRecordIds = this.record.data[field].res_ids
            var table = `<table><thead><tr>`;
            var table_fields = this.nodeOptions['fields'];
            var headers = this.nodeOptions['headers'];
        
            headers.forEach(element => {
                table += '<th>' + element + '</th>';
            });
            table+= `</tr>
                </thead>
                <tbody>`;
            this._rpc({
                model: fieldModel,
                method: 'read',
                args: [fieldRecordIds],
                })
                .then(function(result){
                    Array.from(result).forEach(record => {
                        table+='<tr>'
                        table_fields.forEach(function(key){
                            table += (record[key] ? '<td>' + record[key] + '</td>': '<td></td>');      
                        });
                        table+='</tr>'
                    });
                    table+= `</tbody></table>` 
                    self.$el.append(
                        jQuery(table).attr({
                            'id': 'datatable',
                            'class': 'display',
                        })
                    );
                    jQuery('#datatable').DataTable({searching: false, paging: false, info: false});
                });
                this.$el.find('table').
                prop('disabled', this.mode == 'readonly');
        }
    });
    registry.add('widget_table', FieldMany2OneTable);

    return {
        FieldMany2OneTable: FieldMany2OneTable,        
    }
});

