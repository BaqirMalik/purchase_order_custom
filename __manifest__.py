# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Order Customization',
    'version': '1.0',
    'category': 'Purchase order',
    'sequence': 50,
    'summary': 'Purchase Order',
    'depends': ['purchase'],

    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order.xml',

    ],
    'application': False,

}
