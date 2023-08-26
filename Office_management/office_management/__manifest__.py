{
    'name': 'Office Management',
    'description': '''
    This is For Testing Purpose
    ''',
    'version': '15.0.0.1.0',
    'sequence': 10,
    'author': 'aktiv-softwate',
    'website': 'www.aktiv.com',
    'category': 'Management/Office_Management',
    'depends': ['base', 'sale','contacts'],
    'data': [
        "security/ir.model.access.csv",
        "views/employee_info_views.xml",
        "views/employee_attendance_views.xml",
        "views/manage_task_views.xml",
        "views/employee_salary_views.xml",
        "views/office_expense_views.xml",
        "views/office_department_views.xml",
        "views/employee_skill_views.xml",
        "views/office_designation_views.xml",
        "views/office_information_views.xml",
        "views/office_branch_views.xml",
        "views/sale_task_tab_views.xml",
        "views/hr_inherits_views.xml",
        "views/interviewer_views.xml",
        "views/res_partner_views.xml"

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
