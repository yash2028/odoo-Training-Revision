from odoo import fields, models


class EmployeeSkill(models.Model):
    _name = "employee.skill"
    _description = "Employee Skill Model"
    _rec_name = "skill"

    skill = fields.Char(string="Skill")
    color = fields.Integer(string="Color")
