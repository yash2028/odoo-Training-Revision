from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    hours_assigned = fields.Float(string="H. Assigned")

