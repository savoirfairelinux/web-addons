# -*- coding: utf-8 -*-

from odoo import models, fields, api

class web_widget_table(models.Model):
    _name = 'web_widget_table.web_widget_table'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    task_ids = fields.Many2one(
        string=u'task_ids',
        comodel_name='project.task',
        ondelete='set null',
    )
    

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100