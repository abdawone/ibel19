# -*- coding: utf-8 -*-
{
    'name': "ibel_pos",

    'summary': """
        Customize Ibel POS
        """,
    'description': """
        Customize Ibel POS
    """,

    'author': "Ibel technology",
    'website': "https://ibeltechnology.com",
    'license': 'LGPL-3',

    'category': 'Uncategorized',
    'version': '19.0.1.0.0',
    'depends': ['base','web','point_of_sale'],

    "assets": {
        "point_of_sale._assets_pos": [
            "ibel_pos/static/src/xml/Chrome.xml",
        ],
     },
   'data': [
        'views/templates.xml',
    ],
    "auto_install": True,
}
