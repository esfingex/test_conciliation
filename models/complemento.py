# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class Complemento(models.Model):
    _name = 'complemento'

    concept = fields.Char(string='Concepto')
    type = fields.Char(string='Tipo')
    account = fields.Float(string='Cantidad')
    tax_information = fields.Char(string='Información Impuesto', size=14)
    date = fields.Date(string='Fecha')
    
