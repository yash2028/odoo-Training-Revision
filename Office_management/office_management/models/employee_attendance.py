from odoo import models, fields,api
from datetime import date, datetime, timedelta


class EmployeeAttendance(models.Model):
    _name = "employee.attendance"
    _description = "Employee Attendance Model"

    # name = fields.Char(string="Name", required=True)
    total_leave = fields.Float(string="Total Leave", help="Automatic counted")
    in_time = fields.Datetime(string="In Time")
    out_time = fields.Datetime(string="Out Time")
    break_hours = fields.Float(string="Break Time", help="Automatic counted")
    total_work_hours = fields.Float(string="Total Work Hours", help="Automatic counted", compute='_compute_work_hours', store=1)
    employee_name_id = fields.Many2one('employee.info', string='Name')
    designation = fields.Many2one(related='employee_name_id.designation_id', string="Related Fields", store=True)

    @api.depends('out_time')
    def _compute_work_hours(self):
        for rec in self:
            rec.total_work_hours = 0.0
            if rec.in_time and rec.out_time:
                work_hours = rec.out_time - rec.in_time  # 3:00:00
                print('------work hours--------', work_hours)
                get_minutes = work_hours.total_seconds() // 60  # 10800.0
                print('--------get minutes-------', get_minutes)
                get_hours = int(get_minutes // 60)  # 3
                print('-----------get hours ------------', get_hours)
                total_minute = int(get_minutes % 60)
                print('----------Total minutes-------------', total_minute)
                total_work_hours = float(str(get_hours) + '.' + str(total_minute))
                print('---------total work hours------------', total_work_hours)
                rec.total_work_hours = total_work_hours
