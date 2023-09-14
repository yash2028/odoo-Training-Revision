from odoo import models, fields


class SearchCustomer(models.Model):
    _name = "search.customer"

    customer_id = fields.Many2one('res.partner')
    mobile = fields.Char()
    phone = fields.Char()

    def search_customer(self):
        if self.customer_id:
            action = {
                'type': 'ir.actions.act_window',
                'name': 'Contacts',
                'res_model': 'res.partner',
                'view_mode': 'form',
                'res_id': self.customer_id.id
            }
            return action

    def print_customer(self):
        pass
