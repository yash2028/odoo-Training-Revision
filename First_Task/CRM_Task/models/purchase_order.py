from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_type_id = fields.Many2one(related='partner_id.vendor_id', string="Vendor Type")
