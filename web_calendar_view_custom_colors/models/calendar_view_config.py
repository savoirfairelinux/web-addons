# © 2019 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class CalendarViewConfig(models.Model):
    _name = 'calendar.view.config'

    name = fields.Char(
        string='Description',
        required=True,
    )
    model_id = fields.Many2one(
        string='Calendar Model',
        comodel_name='ir.model',
        required=True,
        help="The model to which the tag rule applies."
    )
    model_name = fields.Char(
        related='model_id.model',
        readonly=True,
    )
    allow_calendar_tag_color = fields.Boolean(
        string='Display calendar with tag colors',
        default=False,
    )
    tag_field_id = fields.Many2one(
        string='Tag Field',
        comodel_name='ir.model.fields',
    )
    tag_field_name = fields.Char(
        string='Tag Field name',
        related='tag_field_id.name',
        readonly=True,
    )
    tag_field_model = fields.Char(
        string='Tag Field Model',
        related='tag_field_id.relation',
        readonly=True,
    )
    color_field_id = fields.Many2one(
        string='Color Tag Field',
        comodel_name='ir.model.fields',
    )
    color_field_name = fields.Char(
        string='Color Tag Field Name',
        related='color_field_id.name',
        readonly=True,
    )
    font_color_field_id = fields.Many2one(
        string='Font Color Tag Field',
        comodel_name='ir.model.fields',
    )
    font_color_field_name = fields.Char(
        string='Font Color Tag Field Name',
        related='font_color_field_id.name',
        readonly=True,
    )
    allow_calendar_hatched = fields.Boolean(
        string='Display calendar with hatched states',
        default=False,
    )
    calendar_state_field_id = fields.Many2one(
        string='Calendar State Field',
        comodel_name='ir.model.fields',
    )
    calendar_state_field_name = fields.Char(
        string='Calendar State Field Name',
        related='calendar_state_field_id.name',
        readonly=True,
    )
    #will be used later to allow many2one state field type
    calendar_state_field_type = fields.Selection(
        string='Calendar State Field Type',
        related='calendar_state_field_id.ttype',
        readonly=True,
    )
    # will be used later to allow many2one state field type
    calendar_state_field_relation = fields.Char(
        string='Calendar State Field Relation',
        related='calendar_state_field_id.relation',
        readonly=True,
    )
    hatched_states = fields.Char(
        string='Calendar Hatched States',
    )

    @api.onchange('model_id')
    def onchange_model_id(self):
        if self.model_id:
            res = {
                'domain': {
                    'tag_field_id': [('model_id', '=', self.model_id.id),
                                     ('ttype', '=', 'many2one')],
                    'calendar_state_field_id': [
                        ('model_id', '=', self.model_id.id),
                        ('ttype', 'in', ['selection', 'many2one'])],
                }
            }
            return res

    @api.onchange('tag_field_id')
    def onchange_tag_field_id(self):
        if self.tag_field_id:
            relation = self.tag_field_id.relation
            res = {
                'domain': {
                    'color_field_id': [('model', '=', relation),
                                       ('ttype', '=', 'char')
                                       ],
                    'font_color_field_id': [
                        ('model', '=', relation),
                        ('ttype', '=', 'selection')]}
            }
            return res

    @api.onchange('calendar_state_field_id')
    def onchange_calendar_state_field_id(self):
        if self.calendar_state_field_id:
            res = {
                'help': {
                        'hatched_states': 'hello',
                }
            }
            return res

    @api.model
    def get_calendar_tag_values(self, model_name):
        def Convert(string):
            li = list(string.split("-"))
            return li
        res = []
        calendar_config = self.env['calendar.view.config'].search(
            [('model_name', '=', model_name)], limit=1)
        if not calendar_config[
            'allow_calendar_tag_color'
        ] and not calendar_config['allow_calendar_hatched']:
            return res
        hatched = False
        color = False
        font_color = False
        calendar_obj = self.env[model_name]
        calendars = calendar_obj.search([])

        if calendar_config:
            for calendar in calendars:
                tag = calendar[calendar_config['tag_field_name']]
                if calendar_config['allow_calendar_hatched'
                ] and calendar_config['hatched_states']:
                    hatched = calendar[calendar_config[
                        'calendar_state_field_name']] in Convert(
                        calendar_config['hatched_states'])
                if calendar_config['allow_calendar_tag_color']:
                    color = tag[calendar_config['color_field_name']]
                    font_color = tag[calendar_config['font_color_field_name']]
                res.append(
                    {
                        'id': calendar.id,
                        'color': color,
                        'font_color': font_color,
                        'hatched': hatched,
                    }
                )
        return res

    @api.model
    def get_calendar_tag_ids(self, model_name):
        # This method is not used for the moment but it may be used later
        res = []
        calendar_tag = self.env['calendar.view.config'].search(
            [('model_name', '=', model_name)], limit=1)

        tag_obj = self.env[calendar_tag['tag_field_model']]
        tags = tag_obj.search([])
        for tag in tags:
            res.append({
                'color': tag[calendar_tag['color_field_name']],
                'id': tag['id']
            }
            )
        return res
