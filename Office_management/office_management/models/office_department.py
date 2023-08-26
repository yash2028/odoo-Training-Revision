from odoo import models, fields


class OfficeDepartment(models.Model):
    _name = "office.department"
    _description = "Office Department Model"
    _rec_name = "dept_name"

    dept_name = fields.Char(string="Department Name", required=True)
    employee_ids = fields.One2many("employee.info", "department_id", string="Employee Details")
    count = fields.Integer(string="Count Of Employee")
    # This is used in office_department_view button type = object
    def call_function(self):
        print('Hello This is for Trial')

    # search count method - ORM
    def count_employee(self):
        print("inside the search count function\n\n\n")
        for rec in self:
            print('Self Value is=============:', self, '\n\n')
            print('rec value is-------------: ', rec)
            print('\n\n\n\n')
            print('Rec id is ===================: ', rec.id)
            sales_count = self.env['employee.info'].search_count([('department_id', '=', rec.id)])
            # developer_count = self.env['employee.info'].search_count([('department_id', '=', 5)])
            # print('Sales Count is :', sales_count)
            # print('\n\n')
            # print('Developer Count is :', developer_count)
            # print('\n\n')
            self.count = sales_count
