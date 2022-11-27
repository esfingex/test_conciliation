# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from xlrd import open_workbook
from odoo import models, api, fields
from odoo.exceptions import ValidationError

class ImportWizardMaster(models.TransientModel):
    _name = 'import.wizard.master'
    _description = 'Importador Datos'
    
    user_id = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user)
    init_date = fields.Date('Fecha Actual', default=lambda self: fields.Datetime.now())
    xlsx_data = fields.Binary('Archivo XLSX', required=True)
    filename = fields.Char()
    
    def load_data(self):
    
        if self.xlsx_data:
            if not self.xlsx_data:
                raise ValidationError("Archivo no encontrado")

        fname = self.filename.split('.')
        ext = fname[len(fname)-1]
        name = fname[0]
        
        if ext != 'xlsx' and name != 'master':
            raise ValidationError("Extensión o nombre incorrecto del archivo")
        
        
        workbook = open_workbook(file_contents=self.xlsx_data)
        sheet_names = workbook.sheet_names()
        sheet = workbook.sheet_by_name(sheet_names[0])
        
        num_rows = sheet.nrows
        
        
    
