from odoo import models, fields, api
import re


class Interviewer(models.Model):
    _name = "interviewer"
    _description = "Interview Process"

    in_first_name = fields.Char(string="Name", required=1)
    in_last_name = fields.Char(string="Name", required=1)
    in_email = fields.Char(string="Email", required=1)
    in_phone = fields.Char(string="Phone", required=1)
    in_city = fields.Char(string="City", required=1)
    in_position = fields.Selection([('erp consultant', 'ERP Consultant'),
                                    ('magento developer', 'Magento Developer'),
                                    ('hr executive', 'HR Executive'),
                                    ('admin executive', 'Admin Executive'),
                                    ('odoo developer', 'Odoo Developer')], string="Position", required=1)
    in_experience = fields.Selection([('fresher', 'Fresher'),
                                      ('zero to one', '0 - 1'),
                                      ('one to two', '1 - 2'),
                                      ('greater than two', ' > 2')], string="Experience", required=1, default='fresher')
    in_linkedin_url = fields.Char(string="LinkedIn Profile URL")
    in_education = fields.Selection([('be', 'B.E.'),
                                     ('btech', 'B.Tech.'),
                                     ('BCA', 'BCA'),
                                     ('mca', 'MCA'),
                                     ('other', 'Other')], string="Education", required=1)
    # in_about = fields.Text(string="Tell me about Your Self")
    in_ref = fields.Selection([('linkedin', 'LinkedIN'),
                               ('website', 'Website'),
                               ('naukri', 'Naukri.Com')], string="Apply in", required=1)
    status = fields.Selection([('s', 'Selected'), ('r', 'Rejected')], string="Status", required=1)

    in_company_name = fields.Char(string="Previous Company Name")
    in_previous_position = fields.Char(string="Previous Position")
    in_previous_salary = fields.Integer(string='Previous CTC')
    interviewer_name = fields.Many2one('employee.info', string="Interviewer Name")
    rejected_brief = fields.Text(string="Why Rejected ?")

    #     on change on email validation

    @api.depends('in_email')
    def ValidateEmail(self):
        print('Hello Everyone\n\n\n\n\n\n\n')