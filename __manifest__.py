# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Test Conciliation',
    'version': '1.0',
    'category': 'Account',
    'description': """ Prueba tecnica""",
    'author': 'Iván Masías - ivan.masias.ortiz@gmail.com',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/master.xml',
        'views/complemento.xml',
        'wizard/import_wizard_master.xml',
        'wizard/import_wizard_complemento.xml',
        'report/concilied_report.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
