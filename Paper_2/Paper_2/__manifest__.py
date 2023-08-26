{
    'name': 'Second Practice Paper',
    'description': '''
    Second Practice Paper
    ''',
    'version': '16.0.0.1.0',
    'sequence': 10,
    'author': 'aktiv-softwate',
    'website': 'www.aktiv.com',
    'category': 'Management/Practice Paper 2',
    'depends': ['base','project'],
    'data': [
        "security/ir.model.access.csv",
        "views/project_project_views.xml",
        "views/project_planning_line_views.xml",
        "views/hr_employee_views.xml"

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}

