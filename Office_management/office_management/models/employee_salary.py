from odoo import models, fields


class EmployeeSalary(models.Model):
    _name = "employee.salary"
    _description = "Employee Salary Model"

    name = fields.Char(string="Name", required=True)
    epf = fields.Selection([('Yes', 'Yes'), ('No', 'No')])
    epf_account_no = fields.Integer(string='EPF Account Number')
    account_no = fields.Integer(string="Account Number", required=True)
    salary = fields.Float(string="Amount", required=True)
    bonus = fields.Float(string="Bonus Amount")
    pan_number = fields.Char(string="PAN Number", required=True)
