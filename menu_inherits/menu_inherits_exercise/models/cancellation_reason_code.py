from odoo import models, fields, api


class CancellationReasonCode(models.Model):
    _name = "cancellation.reason.code"
    # _inherit = "sale.order"

    first_name = fields.Char(string="First Name")
    res_partner = fields.Many2one('res.partner', string="Partner Name", domain=[('head', '=', 'True')])

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        head_count = self.env['res.partner'].search_count([('head', '=', True)])
        # print('Head Count is=================', head_count)
        if head_count == 1:
            get_id = self.env['res.partner'].search([('head', '=', True)])
            # print("get id is==========================", get_id)
            for rec in get_id:
                res['res_partner'] = rec.id
            # print("name is sdhjkfkasd ==========>>>>>>>>>>", rec.name)
        return res
