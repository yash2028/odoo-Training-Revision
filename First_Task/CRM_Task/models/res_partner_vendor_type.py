from odoo import fields, models


class ResPartnerVendorType(models.Model):
    _name = 'res.partner.vendor.type'

    name = fields.Char(string="Vendor Type")
    description = fields.Char(string="Description")






