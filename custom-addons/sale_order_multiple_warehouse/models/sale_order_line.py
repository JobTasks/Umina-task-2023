# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse', readonly=False)

    @api.onchange('warehouse_id')
    def onchange_product_warehouse_id(self):
        self.product_warehouse_id = self.warehouse_id

    def _prepare_procurement_values(self, group_id=False):
        """ Prepare specific key for moves or other components that will be created from a stock rule
        coming from a sale order line. This method could be override in order to add other custom key that could
        be used in move/po creation.
        """
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        if self.product_warehouse_id:
            values.update({'warehouse_id': self.product_warehouse_id})
        return values
