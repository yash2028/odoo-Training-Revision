{
    'name': 'Practice Paper 4',
    'description': '''
        Add Discount in sale module
    ''',
    'version': '15.0.0.1.0',
    'sequence': 10,
    'author': 'aktiv-softwate',
    'website': 'www.aktiv.com',
    'category': 'Management/Practice_Task',
    'depends': ['sale_management','contacts'],
    'report': [
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
        "views/search_customer_views.xml",
        # "report/report_print_customer.xml"


    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
    'auto_install': True,
}
