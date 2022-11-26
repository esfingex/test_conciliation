# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class Complemento(models.Model):
    _name = 'complemento'

    name = fields.Char('Concepto')
    type = fields.Char('Tipo')
    tax_information = fields.Char('Código', size=14)
    account = fields.Float('Cantidad')
    tax_information = fields.Char('Información Impuestos')
    date = fields.Date('res.country', 'Bancos')
    
