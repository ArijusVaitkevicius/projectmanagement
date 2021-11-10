from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'hr.employee'

    leader = fields.Boolean(string="Team leader")
    project_ids = fields.Many2many('projectmanagement.project', string="Projects", readonly=True)
