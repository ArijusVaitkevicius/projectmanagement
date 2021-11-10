# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Invoice(models.Model):
    _name = 'projectmanagement.invoice'
    _description = "Invoices"

    name = fields.Char(string="Invoice title", required=True)

    client_id = fields.Many2one('res.partner', string="Client")
    project_id = fields.Many2one('projectmanagement.project', string="Project")

    status = fields.Selection([
        ('new', "New"),
        ('open', "Open"),
        ('in_progress', "In progress"),
        ('completed', "Completed"),
    ], string="Status", default='new')

