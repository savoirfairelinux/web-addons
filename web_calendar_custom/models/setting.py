# Copyright 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import odoo
from odoo import _, api, fields, models
from odoo.tools import html2plaintext

class Setting(models.Model):
    _name = 'setting'

    name = fields.Char(
        string='Name',
    )

    isActive = fields.Boolean()

    startTime = fields.Float('Starting day hour')

    endTime = fields.Float('Ending day hour')

    startWorkTime = fields.Float('Starting of working time')

    firstDayOfWeek = fields.Selection([('dimanche','Dimanche'), ('lundi', 'Lundi')])

    weekend = fields.Boolean()

    eventOverlap = fields.Boolean()

    minutesPerRow = fields.Integer()


    def get_settings(self):
        return self.env['setting'].browse(1)




