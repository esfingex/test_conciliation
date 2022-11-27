# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import copy

from odoo import models, fields, api

class Master(models.Model):
    _name = 'master'

    date = fields.Date(string='Fecha')
    tax_information = fields.Char(string='Información Impuesto', size=14)
    amount = fields.Float(string='Cantidad')
    bank_id = fields.Many2one('res.bank', string='Bancos')
    country_id = fields.Many2one('res.country', string='País')
    
