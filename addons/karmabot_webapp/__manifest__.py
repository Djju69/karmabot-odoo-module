# -*- coding: utf-8 -*-
{
    'name': 'KarmaBot WebApp',
    'version': '1.0.0',
    'category': 'Tools',
    'summary': 'KarmaBot WebApp Module',
    'description': """
        KarmaBot WebApp Module
        =====================
        
        Простой модуль для интеграции с KarmaBot
    """,
    'author': 'KarmaBot Team',
    'website': 'https://karmabot.com',
    'depends': ['base', 'web', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/webapp_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'karmabot_webapp/static/src/css/webapp.css',
            'karmabot_webapp/static/src/js/webapp.js',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}