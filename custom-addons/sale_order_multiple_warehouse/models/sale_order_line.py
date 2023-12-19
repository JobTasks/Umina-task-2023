# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse', readonly=False)

    @api.onchange('warehouse_id')
    def onchange_product_warehouse_id(self):
        self.product_warehouse_id = self.warehouse_id

