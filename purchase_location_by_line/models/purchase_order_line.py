# © 2016 ForgeFlow S.L.
#   (<http://www.forgeflow.com>)
# © 2018 Hizbul Bahar <hizbul25@gmail.com>
# © 2026 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    location_dest_id = fields.Many2one(
        comodel_name="stock.location",
        string="Destination",
        domain=[("usage", "in", ["internal", "transit"])],
    )

    def _purchase_split_date_get_group_keys(self, picking):
        key = super()._purchase_split_date_get_group_keys(picking)
        default_picking_location_id = self.order_id._get_destination_location()
        default_picking_location = self.env["stock.location"].browse(
            default_picking_location_id
        )
        location = self.location_dest_id or default_picking_location
        return key + (("location_dest_id", location.id),)

    def _purchase_split_date_get_sorted_keys(self):
        keys = super()._purchase_split_date_get_sorted_keys()
        return keys + (self.location_dest_id.id,)

    def _prepare_stock_moves(self, picking):
        if (
            picking
            and self.location_dest_id
            and not picking.move_ids
            and picking.location_dest_id != self.location_dest_id
        ):
            picking.location_dest_id = self.location_dest_id

        res = super()._prepare_stock_moves(picking)

        if self.location_dest_id:
            for vals in res:
                vals["location_final_id"] = self.location_dest_id.id
                vals["location_dest_id"] = self.location_dest_id.id
        return res
