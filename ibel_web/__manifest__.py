# -*- coding: utf-8 -*-
{
    'name': "ibel_web",

    'summary': """
        Customize Ibel backend
        """,
    'description': """
        Customize Ibel backend
    """,

    'author': "Ibel technology",
    'website': "https://ibeltechnology.com.com",
    'license': 'LGPL-3',

    'category': 'Uncategorized',
    'version': '19.0.1.0.0',
    'depends': ['base','base_import_module',],

 
    "assets": {
        "web.assets_backend": [
            "ibel_web/static/src/**/*",
        ],
    },
   'data': [
        'views/webclient_templates.xml',
    ],
    "installable": True,
    "auto_install": True,
}
