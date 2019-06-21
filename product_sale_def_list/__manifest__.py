# -*- coding: utf-8 -*-
{
    'name': "Product default list (tree) view in the sale module", 
    'version': '12.0.0.99.15',
    'category': 'Sales',
    'depends': ['sale'],
    'license': 'AGPL-3',
    'summary': 'Set list (tree) as a default view for product in the Sale module',
    'description': """
Changes default view of product to a list (tree) in the Sale module
========================================================================
    """,
    'installable': True,
    'auto_install': False,
    'author': "odoocraft.com",
    
    
    'images': [
        'images/main_screenshot.png',
        ],
    'data': [
        'views/views.xml',
    ],
}
