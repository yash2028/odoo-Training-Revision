{
    'name': 'Menu Inheritance',
    'description': '''
    menu inherits & model inherits
    ''',
    'version': '15.0.0.1.0',
    'sequence': 10,
    'author': 'aktiv-softwate',
    'website': 'www.aktiv.com',
    'category': 'Management/menu_inherits',
    'depends': ['base','sale','purchase'],
    'data': [
        "security/ir.model.access.csv",
        "views/cancellation_reason_code.xml",
        "views/contacts_views.xml",
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
