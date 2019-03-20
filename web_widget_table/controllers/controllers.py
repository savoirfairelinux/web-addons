# -*- coding: utf-8 -*-
from odoo import http

# class WebWidgetTable(http.Controller):
#     @http.route('/web_widget_table/web_widget_table/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_widget_table/web_widget_table/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_widget_table.listing', {
#             'root': '/web_widget_table/web_widget_table',
#             'objects': http.request.env['web_widget_table.web_widget_table'].search([]),
#         })

#     @http.route('/web_widget_table/web_widget_table/objects/<model("web_widget_table.web_widget_table"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_widget_table.object', {
#             'object': obj
#         })