{
    'name': 'TASK 1',
    'description': '''
    This is For Testing Purpose
    ''',
    'version': '15.0.0.1.0',
    'sequence': 10,
    'author': 'aktiv-softwate',
    'website': 'www.aktiv.com',
    'category': 'Management/CRM_Task',
    'depends': ['base','crm','sale','purchase'],
    'data': [
        "security/ir.model.access.csv",
        "views/crm_lead_views.xml",
        "views/res_partner_vendor_type_views.xml",
        "views/res_partner_views.xml",
        "views/purchase_order_views.xml",
        "views/sale_order_views.xml"

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
