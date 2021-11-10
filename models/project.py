# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _name = 'projectmanagement.project'
    _description = 'Projects'

    name = fields.Char(string='Project title', required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")

    client_id = fields.Many2one('res.partner', string="Client")
    leader_id = fields.Many2one('hr.employee', string="Team Leader", domain=[('leader', '=', True)])
    employees_ids = fields.Many2many('hr.employee', string="Employee")
    jobs_ids = fields.One2many('projectmanagement.job', 'project_id', string="Jobs")
    invoice_ids = fields.One2many('projectmanagement.invoice', 'project_id', string="Invoices")

    status = fields.Selection([
        ('new', "New"),
        ('open', "Open"),
        ('in_progress', "In progress"),
        ('completed', "Completed"),
    ], string="Status", default='new')



