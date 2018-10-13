# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/LGPL).

{
    'name': 'Calendar Custom Settings',
    'version': '0.1',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'https://www.savoirfairelinux.com',
    'license': 'LGPL-3',
    'category': 'Web',
    'summary': 'Change default calendar settings',
    'depends': [
        'web',
    ],
    'data': [
        'data/default_data.xml',
        'data/ir_config_parameter.xml',
        'views/web_calendar_custom.xml',
        'views/res_config_views.xml',
        'static/src/js/web_calendar_custom.js'
    ],
    'installable': True,
    'application': True,
}
