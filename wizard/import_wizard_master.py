# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from base64 import b64decode

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
        
        if ext != 'xlsx':
            raise ValidationError("Extensión incorrecto del archivo")
        
        if name != 'master':
            raise ValidationError("Nombre de archivo incorrecto")
        
        workbook = open_workbook(file_contents=b64decode(self.xlsx_data))
        sheet_names = workbook.sheet_names()
        sheet = workbook.sheet_by_name(sheet_names[0])
        
        num_rows = sheet.nrows - 1
        num_cols = sheet.ncols - 1
        
        #Cabecera archivo master.xlsx
        head = ['date', 'tax_information', 'amount', 'bank_id', 'country_id']
    
        #Valida la cabecera del archivo
        if sheet._cell_values[0] != head:
            raise ValidationError("Encabezado no existe, favor agregar encabezado")
        else:
            data = []
            for i in range(1, num_cols):
                if '' not in sheet._cell_values[i]:
                    value = dict(zip(head, sheet._cell_values[i]))
                    data.append((0,0,value))
                else:
                    raise ValidationError(("Datos vacios en la linea %s") % i)
            self.env['master'].create(data)
        
        