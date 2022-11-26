# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import copy

from odoo import models, fields, api

class Master(models.Model):
    _name = 'master'

    name = fields.date('Fecha')
    tax_information = fields.Char('Código', size=14)
    amount = fields.Float('Cantidad')
    bank_id = fields.Many2one('res.bank', 'Bancos')
    country_id = fields.Many2one('res.country', 'Bancos')
    
