# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from xlrd import open_workbook
from odoo import models, api, fields

class ImportWizardComplemento(models.TransientModel):
    _name = 'import.wizard.complemento'
    _description = 'Importador Datos'
    
    user_id = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user)
    init_date = fields.Date('Fecha Actual', default=lambda self: fields.Datetime.now())
    xlsx_data = fields.Binary('Archivo XLSX', required=True)
    
    def load_data(self):
        
        workbook = open_workbook(file_contents=self.xlsx_data)
        sheet_names = workbook.sheet_names()
        sheet = workbook.sheet_by_name(sheet_names[0])
        
        num_rows = sheet.nrows
        
        
    
