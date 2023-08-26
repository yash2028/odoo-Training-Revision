from odoo import fields, models, api


class OfficeBranch(models.Model):
    _name = "office.branch"
    _description = "Office Branch Model"
    _rec_name = "country_name"

    office_id = fields.Many2one("office.information", string="Office Name")
    country_name = fields.Char(string="Country Name")

    employee_ids = fields.One2many("employee.info", "country_id", string="Employees")

    # create method
    @api.model
    def create(self, vals):
        print('>>>>>> SELF >>>>>>>', self)
        print(">>>>>>>>> VALS <<<<<<<<<<<", vals)
        res = super().create(vals)
        print("+++++++++++++++++ RES ___", res)
        return res

    def write(self, vals):
        print('>>>>>>write SELF >>>>>>>', self)
        print(">>>>>>>>> write VALS <<<<<<<<<<<", vals)
        res = super().write(vals)
        print("+++++++++++++++++ RES ___", res)
        print("SELF ENV IS:     ",dict(self.env))
        return res
