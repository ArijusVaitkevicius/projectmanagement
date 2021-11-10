# -*- coding: utf-8 -*-
{
    'name': "Project Management",

    'summary': """Manage projects""",

    'description': """
        Project Management module for managing projects:
            - projects
            - tasks
            - team leads
            - employees
            - clients
            - invoices
    """,

    'author': "Arijus Vaitkevičius",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/job_view.xml',
        'views/invoice_view.xml',
        'views/partner_inherited_view.xml',
        'views/employee_inherited_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install': True,
}