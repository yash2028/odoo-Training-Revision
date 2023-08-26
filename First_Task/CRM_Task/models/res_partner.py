from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vendor_id = fields.Many2one('res.partner.vendor.type', string="Vendor Type")



