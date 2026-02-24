# © 2016 ForgeFlow S.L.
#   (<http://www.forgeflow.com>)
# © 2018 Hizbul Bahar <hizbul25@gmail.com>
# © 2026 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Purchase Location by Line",
    "summary": "Allows to define a specific destination location on each PO line",
    "version": "19.0.1.0.0",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "contributors": ["scalizer"],
    "website": "https://github.com/OCA/purchase-workflow",
    "category": "Purchase Management",
    "depends": ["purchase_stock", "purchase_delivery_split_date"],
    "license": "AGPL-3",
    "data": ["views/purchase_views.xml"],
    "installable": True,
}
