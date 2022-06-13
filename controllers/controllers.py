# -*- coding: utf-8 -*-
# from odoo import http


# class Warteg(http.Controller):
#     @http.route('/warteg/warteg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/warteg/warteg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('warteg.listing', {
#             'root': '/warteg/warteg',
#             'objects': http.request.env['warteg.warteg'].search([]),
#         })

#     @http.route('/warteg/warteg/objects/<model("warteg.warteg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('warteg.object', {
#             'object': obj
#         })
