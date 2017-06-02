# -*- coding: utf-8 -*-
# © 2017 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "UI Color Env",
    "version": "10.0.1.0.0",
    "author": "Savoir-faire Linux",
    'maintainer': "Savoir-faire Linux",
    'website': 'http://www.savoirfairelinux.com',
    'license': 'LGPL-3',
    "category": "UI",
    "summary": "UI color for customers lab env",
    'description':
    """
    For Odoo Enterprise Version 10.0, this module replaces the default Odoo color palette with the color palette as defined in the less variables.
    This module is based on the work of Bista Solutions. https://github.com/bistaray/odoo-apps#10.0
    """,
    "depends": ["base"],
        "data": [
        'views/color_change.xml',
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}
