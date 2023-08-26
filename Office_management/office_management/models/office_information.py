from odoo import models, fields

class OfficeInformation(models.Model):
    _name = "office.information"
    _description = "Office Information Model"
    _rec_name = "office_name"

    office_name = fields.Char(string="Office Name")
    office_address = fields.Text(string="Office Address")
    office_since = fields.Integer(string="Opening Year")
    office_contact = fields.Char(string="Contact Number")
    office_email = fields.Char(string="Email Address")