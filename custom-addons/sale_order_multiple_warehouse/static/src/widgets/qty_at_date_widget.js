/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { QtyAtDatePopover } from "@sale_stock/widgets/qty_at_date_widget";


patch(QtyAtDatePopover.prototype, {
    openForecast() {
        this.actionService.doAction("stock.stock_forecasted_product_product_action", {
            additionalContext: {
                active_model: 'product.product',
                active_id: this.props.record.data.product_id[0],
                warehouse: this.props.record.data.product_warehouse_id && this.props.record.data.product_warehouse_id[0],
                move_to_match_ids: this.props.record.data.move_ids.records.map(record => record.resId),
                sale_line_to_match_id: this.props.record.resId,
            },
        });
    }
});