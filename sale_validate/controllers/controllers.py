# -*- coding: utf-8 -*-
from odoo import http

# class SaleValidate(http.Controller):
#     @http.route('/sale_validate/sale_validate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_validate/sale_validate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_validate.listing', {
#             'root': '/sale_validate/sale_validate',
#             'objects': http.request.env['sale_validate.sale_validate'].search([]),
#         })

#     @http.route('/sale_validate/sale_validate/objects/<model("sale_validate.sale_validate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_validate.object', {
#             'object': obj
#         })