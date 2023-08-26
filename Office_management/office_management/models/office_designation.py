from odoo import models, fields


class OfficeDesignation(models.Model):
    _name = "office.designation"
    _description = "Office Designation Model"
    _rec_name = "designation_name"

    designation_name = fields.Char(string="Designation")
