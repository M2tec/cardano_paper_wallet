# -*- coding: utf-8 -*-
{
    'name': 'Cardano paper wallet',
    'version': '13.0.1.0',
    'summary': """
      Generate a new cardano wallet
       """,
    'category': 'Point of Sale',
    'author': 'Maarten Menheere',
    'description': """Add a button to gerenerate a new wallet for the cardano blockchain""",
    'website': 'https://www.m2tec.nl',
    'depends': ['base', 'point_of_sale', 'pos_restaurant'],
    'data': [
        'views/view.xml',
        'views/pos_order.xml',
        'views/pos_config_views.xml',
    ],
    'qweb': [
        'static/src/xml/ReceiptScreen.xml'
    ],
    'images': ['static/description/thumbnail.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,

}
