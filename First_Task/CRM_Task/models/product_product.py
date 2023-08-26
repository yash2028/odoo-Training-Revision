from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def name_get(self):
        record = []
        for detail in self:
            if not detail.default_code:
                name = detail.name
            else:
                name = detail.default_code
            record.append((detail.id, name))
        return record
