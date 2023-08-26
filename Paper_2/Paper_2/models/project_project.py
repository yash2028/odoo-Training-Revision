from odoo import fields, models, api


class Project(models.Model):
    _inherit = "project.project"

    hours_total = fields.Float(string="Hours Project")
    hours_total_planned = fields.Float(string="Hours Total Planned", compute="_compute_hours_total_plannned", store=1)  # Computed Field ( hours total - sum (One2many
    # field))
    planning_line_ids = fields.One2many('project.planning.line', 'project_id', string="Planning Hours")
    # name = fields.Char()

    @api.depends('hours_total','planning_line_ids.hours_invested')
    def _compute_hours_total_plannned(self):
        for rec in self:
            rec.hours_total_planned = self.hours_total - sum(rec.planning_line_ids.mapped('hours_invested'))
            print("\n\n\n\n\n\n\n\nHello Project.Project Module",sum(rec.planning_line_ids.mapped('hours_invested')))


