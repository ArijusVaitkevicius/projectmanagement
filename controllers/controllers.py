# -*- coding: utf-8 -*-
# from odoo import http


# class Projectmanagement(http.Controller):
#     @http.route('/projectmanagement/projectmanagement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projectmanagement/projectmanagement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('projectmanagement.listing', {
#             'root': '/projectmanagement/projectmanagement',
#             'objects': http.request.env['projectmanagement.projectmanagement'].search([]),
#         })

#     @http.route('/projectmanagement/projectmanagement/objects/<model("projectmanagement.projectmanagement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projectmanagement.object', {
#             'object': obj
#         })
