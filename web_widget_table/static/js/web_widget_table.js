odoo.define('web_widget_table', function(require)
{
    var registry = require('web.field_registry'),
        AbstractField = require('web.AbstractField'),
        FieldMany2OneTable = AbstractField.extend({
        className: 'oe_form_field_table',
        supportedFieldTypes: ['many2one','char'],
        init: function()
        {
            this._super.apply(this, arguments);
        },
        _render: function()
        {
            this.$el.empty(); 
            var field = this.nodeOptions['field_name'],
                fieldModel = this.record.data[field].model,
                fieldRecordIds = this.record.data[field].res_ids,
                table = `<table><thead><tr>`,
                table_fields = this.nodeOptions['fields'],
                headers = this.nodeOptions['headers'];
                searching = this.nodeOptions['searching'];
                paging = this.nodeOptions['paging'];
                info = this.nodeOptions['info'],
                datatable_params = this.nodeOptions['datatable_params'];

            headers.forEach(element => {
                table += '<th>' + element + '</th>';
            });
            table+= `</tr></thead><tbody>`;
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
                    table+= `</tbody></table>`;
                    this.$el.append(
                        jQuery(table).attr({
                            'id': 'datatable',
                            'class': 'display',
                        })
                    );
                    jQuery('#datatable').DataTable(datatable_params);
                }.bind(this));             
        }
    });
    registry.add('widget_table', FieldMany2OneTable);

    return {
        FieldMany2OneTable: FieldMany2OneTable,        
    }
});
