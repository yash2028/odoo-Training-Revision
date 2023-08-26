from odoo import fields, models


class SaleTaskTab(models.Model):
    _inherit = "sale.order"

    commission_type = fields.Selection([('fixed', 'Fixed'), ('percentage', 'Percentage')])
    commission_amount = fields.Float(string="Amount")
    commission_agent_id = fields.Many2one('res.partner', string="Agent Name")

    state = fields.Selection(selection_add=[('approved', 'Approved')])
