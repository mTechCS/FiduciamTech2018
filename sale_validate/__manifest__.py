# -*- coding: utf-8 -*-
{
    'name': "Sale Validate",

    'summary': """
        Sales Order Validate that only Sales Manager can confirm sales order""",

    'description': """
        Sales Order Validate that only Sales Manager can confirm sales order
    """,

    'author': "MTechCS (ubaid@mtechcs.com)",
    'website': "http://mtechcs.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '11.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}