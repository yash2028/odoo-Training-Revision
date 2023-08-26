from odoo import fields, models, api


class ProjectPlanningLine(models.Model):
    _name = 'project.planning.line'

    project_id = fields.Many2one('project.project', string="Project")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    hours_invested = fields.Float(string="H Invested", compute="_compute_hours_invested", store=1)
    hours_assigned = fields.Float(string="H Assigned")
    hours_assigned_string = fields.Char(string="H. Assigned")
    hour_pending = fields.Float("H Pending", compute="_compute_hour_pending", store=1)
    hours_pending_string = fields.Float("H. Pending")

    @api.depends('project_id', 'employee_id')
    def _compute_hours_invested(self):
        total = 0.0
        for rec in self.project_id.timesheet_ids:
            if rec.employee_id == self.employee_id:
                total += rec.unit_amount
        self.hours_invested = total

    @api.depends('hours_assigned')
    def _compute_hour_pending(self):
        self.hour_pending = self.hours_invested - self.hours_assigned
