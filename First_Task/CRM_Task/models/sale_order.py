from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_contact = fields.Char(string="Contact")



