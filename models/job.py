# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Job(models.Model):
    _name = 'projectmanagement.job'
    _description = "Jobs"

    name = fields.Char(string="Job title", required=True)

    project_id = fields.Many2one('projectmanagement.project', string="Project")
