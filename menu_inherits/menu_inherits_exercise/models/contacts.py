from odoo import models, fields, api


class contact(models.Model):
    _inherit = "res.partner"

    head = fields.Boolean(string="Head or Not ?")

    def name_get(self):
        result = []
        for contact in self:
            name = contact.name + " [" + contact.phone + " ]"
            result.append((contact.id, name))
        print("++++++++++++++++++++++=", result)
        return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if args is None:
            args = []
        domain = args + ['|', '|', ('name', operator, name), ('email', operator, name), ('phone', operator, name)]
        print('HELLO', domain)
        # abc = self._search(domain, limit=limit, access_rights_uid=name_get_uid)
        # print("ABC ABC IS: ", abc)
        return self._search(domain, limit=limit, access_rights_uid=name_get_uid)
