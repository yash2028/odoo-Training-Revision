from odoo import models, fields


class ManageTask(models.Model):
    _name = "manage.task"
    _description = "Employee Assign Task"

    task_name = fields.Char(string="Task name")
    task_desc = fields.Text(string="Task description")
    submit_time = fields.Datetime(string="Task submit time")
    priority = fields.Selection([('0', 'zero'), ('Low', 'Low'),
                                 ('Medium', 'Medium'), ('High', 'High')])
    assign_by = fields.Char(string="Assigned by")
    assign_to = fields.Char(string="Assigned to")
