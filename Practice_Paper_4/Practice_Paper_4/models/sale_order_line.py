from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    discount_method = fields.Selection(
        [('fixed', 'Fixed'),
         ('percentage', 'Percentage')])
    discount_amount = fields.Float()
    product_category_id = fields.Many2one('product.category')

    @api.onchange('product_category_id')
    def _onchange_product_category(self):
        if self.product_category_id:
            return {
                'domain': {'product_id': [('categ_id', '=', self.product_category_id.id)]},
                'context': {
                    'default_product_category_id': self.product_category_id.id,
                }
            }
        else:
            return {
                'domain': {'product_id': []},
                'context': {
                    'default_product_category_id': False,
                }
            }

