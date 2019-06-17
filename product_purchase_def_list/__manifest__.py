# -*- coding: utf-8 -*-
{
    'name': "Product list (tree) view in purchase module", 
    'version': '12.0.0.99.10',
    'category': 'Purchases',
    'depends': ['purchase','product'],
    'license': 'LGPL-3',
    'summary': 'Set list (tree) as a default view for product in Purchase module',
    'description': """
Changes default view of product to list (tree) in Purchase module
========================================================================
    """,
    'installable': True,
    'auto_install': False,
    'author': "odoocraft.com",
    
    
    'images': [
        'images/main_screenshot.png'
        ],
    'data': [
        'views/views.xml',
    ],
    'demo': [
    ],
}
