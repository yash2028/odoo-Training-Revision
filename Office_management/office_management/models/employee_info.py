from odoo import models, fields, api
from datetime import date, datetime


class EmployeeInfo(models.Model):
    _name = "employee.info"
    _description = "Employee Information Model"
    # _inherits = {"res.partner": "partner_id"}
    # _inherit = "sale.order"
    _rec_name = "name"

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    mobile_no = fields.Integer(string="Mobile_No.")
    date_of_birth = fields.Date(string="Date Of Birth")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    image = fields.Image(string="Image")
    position = fields.Char(string="position")
    shift_time = fields.Selection(
        [('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Night', 'Night')])
    salary = fields.Integer(string="Salary")
    date_of_joining = fields.Date(string="Date of Joining")
    department_id = fields.Many2one("office.department", string="Department")
    emp_skill_ids = fields.Many2many("employee.skill", "employee_skill_rel", "emp_id", "skill_id", string="Skills")
    designation_id = fields.Many2one("office.designation", string="Designation")
    office_id = fields.Many2one("office.information", string="Office Name")
    country_id = fields.Many2one("office.branch", string="Branch Name")
    partner_id = fields.Many2one("res.partner", strring="Partner id")
    # This field for onchange method
    email = fields.Char(string="Email")
    # website = fields.Char(string="Website")
    is_employee = fields.Boolean(string="is employee ?")
    # computes fields
    work_days = fields.Integer(string='Working Days', compute='_compute_working_days', store=True)
    name = fields.Char(string="Name", compute='_compute_full_name', inverse="_set_record_names")
    status = fields.Selection([('trainee', 'Trainee'), ('employee', 'Employee')], default="trainee")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        print("\n\n\n\n\n\n", self)
        self.email = self.partner_id.email
        self.website = self.partner_id.website
        self.is_employee = self.partner_id.is_employee

    # Calculate working days
    @api.depends('date_of_joining')
    def _compute_working_days(self):
        print('--------Calling Function------------')
        for rec in self:
            print('----------Inside the for loop----------------')
            print('-----------self---------------------', self)
            rec.work_days = 0
            today_date = date.today()
            if rec.date_of_joining:
                total_days = today_date - rec.date_of_joining
                rec.work_days = total_days.days

    def _compute_full_name(self):
        for rec in self:
            if rec.first_name or rec.last_name:
                com_full_name = str(rec.first_name) + ' ' + str(rec.last_name)
                rec.name = com_full_name

    # inverse method
    def _set_record_names(self):
        for rec in self:
            if rec.name:
                get_names = rec.name.split()
                if len(get_names) == 2:
                    rec.first_name = get_names[0]
                    rec.last_name = get_names[1]
                else:
                    pass

    # search method - ORM
    def search_employee(self):
        condition1 = ('email', '=', 'yash@gmail.com')
        condition2 = ('first_name', '=', 'Dev')
        condition3 = ('last_name', '=', 'Parekh')
        employee_ids = [86, 87, 89]
        employee_fields = ['first_name', 'last_name']
        search_read = self.env['employee.info'].search([])
        print(search_read, '===========================================')
        print('\n\n\n\n\n\n\n\n\n')
        # print('Read Method is:                           ', search_read.read([]))
        print('Read Method is:                           ', self.env['employee.info'].search([]).read(employee_fields))
        print('\n\n\n\n\n')
        print('Search Read Method is:                      ', search_read.search_read(['|', ('first_name', '=', 'Yash'), ('first_name', '=', 'Vikas')], fields=['first_name', 'last_name'], limit=2))
        print('\n\n\n\n\n')
        print('search Group Method is:                     ', search_read.read_group([('office_id', '=', 'Aktiv')], fields=None , groupby='gender'))

        # search_val = self.env['employee.info'].search([('first_name', '=', 'Yash')], limit=1)
        search_val = self.env['employee.info'].search([('id', '=', 123)])
        print("\n\n\nPrint Employee infor env method", search_val)
        for rec in search_val:
            print("rec is: ", rec)
            print("Name is: ", rec.name)
        # search_val1 = self.env['employee.info'].search(['|', condition1, '&', condition2, condition3])
        # print("\n\n\nPrint Employee info1111 env method", search_val)
        print("\n\n\nPrint Employee infor1111111111 env method", search_val)

    # Browse method - ORM
    def browse_employee(self):
        print('\n\n\n\n')
        # domain = [('id', '=', 123)]
        employees = self.env['employee.info'].browse([123])
        print('Inside the browse methods: ', employees)
        print('\n\n\n')
        for rec in employees:
            print('Full Name is: ', rec.name)
            print('\n')

    # default_get same as default
    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        print("Before the default value >>>>>>>>>>>>>>>>>>>>>>>", res)
        res['first_name'] = 'odoo'
        res['last_name'] = 'admin'
        print("after the default value <<<<<<<<<<<<<<<<<<<<<<<<", res)
        return res

    # create method
    @api.model
    def create(self, vals):
        print("create call==============\n\n")
        res = super(EmployeeInfo, self).create(vals)
        print("Welcome==========First Call super", res)
        print("Vals=============", vals)
        print("Self=============", self)
        if vals.get('gender') == 'male':
            print('Inside the condition=================')
            res['first_name'] = 'Mr. ' + res['first_name']
        elif vals.get('gender') == 'female':
            res['first_name'] = 'miss ' + res['first_name']
        else:
            return res
        # print('\n\n\n\n\n\n')
        # print("Hello This is -=========================================")
        # res_after = super().create(vals)
        #
        # print("BYE BYE============", res_after)
        #
        # return res_after

        #
        return res


class NewResPartner(models.Model):
    _inherit = "res.partner"
    # this field add to res.partner form
    is_employee = fields.Boolean(string='Employee ?')
