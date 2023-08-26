from odoo import models, fields


class HrInherits(models.Model):
    _name = "hr.inherits"
    _inherits = {'employee.info': 'employee_info_id'}

    # employee_info_id = fields.Many2one('employee.info', string="Employee Name")
    position_hr = fields.Boolean(string="New Joined")
