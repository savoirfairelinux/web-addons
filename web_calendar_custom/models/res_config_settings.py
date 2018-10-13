# Copyright 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    calendar_start_time = fields.Char('Calendar Start Time')
    calendar_end_time = fields.Char('Calendar End Time')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            calendar_start_time=self.env[
                'ir.config_parameter'].sudo().get_param(
                'web_calendar_custom.calendar_start_time'),
            calendar_end_time=self.env[
                'ir.config_parameter'].sudo().get_param(
                'web_calendar_custom.calendar_end_time'),
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'web_calendar_custom.calendar_start_time',
            self.calendar_start_time)
        self.env['ir.config_parameter'].sudo().set_param(
            'web_calendar_custom.calendar_end_time',
            self.calendar_end_time)
