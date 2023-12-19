# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Multiple Warehouse',
    'version': '1.0',
    'category': 'Sales/Sales',
    'sequence': 55,
    'summary': 'Sale Order Multiple Warehouse',
    'depends': [
        'sale_management',
        'stock'
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sale_order_multiple_warehouse/static/src/**/*',
        ],
    },
    'application': True,
}
