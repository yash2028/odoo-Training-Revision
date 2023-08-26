from odoo import models, fields


class OfficeExpense(models.Model):
    _name = "office.expense"

    office_name = fields.Char(string="office_name", required=True)
    events = fields.Selection([('Events', 'Events'), ('Tours', 'Tours')])
    event_date = fields.Date(string="Event Date")
    cost = fields.Float(string="Cost")
    event_description = fields.Text(string="Event Description")
    venue = fields.Text(string="Events Venue")
    buy_product = fields.Char(string="Buy_Product")
    sr_number = fields.Char(string="Sr Number")
    price = fields.Float(string="Price")
