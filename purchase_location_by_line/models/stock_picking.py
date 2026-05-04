# © 2026 Scalizer (<https://www.scalizer.fr>)
import logging

from odoo import api, models
from odoo.fields import Domain

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.model
    def _purchase_split_date_assign_domain(self, key, tz):
        domain = super()._purchase_split_date_assign_domain(key, tz)
        location_dest_id = False
        for key_element in key:
            if (
                isinstance(key_element, (tuple, list))
                and len(key_element) == 2
                and key_element[0] == "location_dest_id"
            ):
                location_dest_id = key_element[1]
                break

        if location_dest_id:
            domain = Domain.AND(
                [
                    domain,
                    [("location_dest_id", "=", location_dest_id)],
                ]
            )
            return list(domain)
        return domain
