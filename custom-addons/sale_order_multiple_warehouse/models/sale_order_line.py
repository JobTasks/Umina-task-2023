# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse', readonly=False)

    @api.onchange('warehouse_id')
    def onchange_product_warehouse_id(self):
        self.product_warehouse_id = self.warehouse_id

    def _prepare_procurement_values(self, group_id=False):
        """Create multiple deliveries by grouping warehouses in sale order lines.

        If there are two sale order lines with same product it will be grouped to same delivery.
        """
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        if self.product_warehouse_id:
            values.update({'warehouse_id': self.product_warehouse_id})
        return values
