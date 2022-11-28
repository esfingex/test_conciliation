# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, tools, api


class ConciledReport(models.Model):
    _name = 'conciled.report'
    _description = "Conciliación"
    _auto = False
    _order = "date asc"

    id = fields.Integer('ID')
    date = fields.Date(string='Fecha', readonly=True)
    tax_information = fields.Char(string='Información Impuesto', readonly=True)
    amount = fields.Float(string='Cantidad', readonly=True)
    bank_id = fields.Many2one('res.bank', string='Bancos', readonly=True)
    country_id = fields.Many2one('res.country', string='País', readonly=True)
    concept = fields.Char(string='Concepto', readonly=True)
    type = fields.Char(string='Tipo', readonly=True)
    account = fields.Float(string='Cantidad', readonly=True)
    
    def _select(self):
        return """
            SELECT
                m.id,
                m.date,
                m.tax_information,
                m.amount,
                m.bank_id,
                m.country_id,
                c.concept,
                c.type,
                c.account
            FROM master AS m
            JOIN complemento AS c ON m.tax_information = c.tax_information
        """

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                %s
            )
        """ % (self._table, self._select())
        )
