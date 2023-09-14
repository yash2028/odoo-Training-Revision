from odoo import fields, models, api
import json


class SaleOrder(models.Model):
    _inherit = "sale.order"

    discount_applies_to = fields.Selection([('global', 'Global'), ('order_line', 'Order Line')])
    discount_method = fields.Selection([('fixed', 'Fixed'), ('percentage', 'Percentage')])
    discount_amount = fields.Float()
    total_discount = fields.Float(readonly=True, compute='_compute_total_discount', store=True)

    @api.depends('discount_amount', 'order_line.discount_method')
    def _compute_total_discount(self):
        for rec in self:
            rec.total_discount = 0.0
            if rec.discount_method == 'fixed':
                rec.total_discount = rec.discount_amount
                rec.amount_total -= rec.discount_amount
                if not rec.amount_total == rec.amount_untaxed:
                    rec.amount_untaxed -= rec.discount_amount
            elif rec.discount_method == 'percentage':
                value = (rec.discount_amount / 100 * rec.amount_untaxed)
                rec.total_discount = value
                rec.amount_total -= value
                if not rec.amount_total == rec.amount_untaxed:
                    rec.amount_untaxed -= value
            else:
                rec.total_discount = 0.0
                discount_sum = 0.0
                for each_product in rec.order_line:
                    if each_product.discount_method == 'fixed':
                        discount_sum += each_product.discount_amount

                    elif each_product.discount_method == 'percentage':
                        value = (each_product.discount_amount / 100 * each_product.price_subtotal)
                        discount_sum += value

                    rec.total_discount = discount_sum

                rec.amount_total -= rec.total_discount
                if not rec.amount_total == rec.amount_untaxed:
                    rec.amount_untaxed -= rec.total_discount

