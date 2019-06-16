{
    'name': "product_purchase_def_list_view", 
    'summary': """
        Set list (tree) as a default view for product in Purchase module""",
    'description': """
        Changes default view of product to list (tree) in Purchase module
    """,
    'version': '12.0.0.99.10',
    'category': 'Purchases',
    'depends': ['purchase'],
    'license': 'LGPL-3',
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
    'depends': ['base'],
}
