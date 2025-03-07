# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Bulgaria - Intrastat Product Declaration',
    'version': '16.0.1.0.1',
    'category': 'Intrastat',
    'license': 'AGPL-3',
    "website": "https://github.com/rosenvladimirov/l10n-bulgaria",
    'summary': 'Intrastat Product Declaration for Bulgaria',
    'author': "Rosen Vladimirov <vladimirov.rosen@gmail.com>, ",
    'depends': [
        'base',
        'l10n_bg',
        'l10n_bg_city',
        'l10n_bg_config',
        'base_address_extended',
        'intrastat_product',
        'intrastat_product_hscodes_import',
        'partner_fax',
    ],
    'conflicts': [
        'l10n_bg_intrastat',
        'report_intrastat',
        'intrastat_product_generic',
    ],
    'data': [
        'data/intrastat.region.csv',
        'data/res.city.csv',
        # 'data/intrastat_unit.xml',
        'security/intrastat_security.xml',
        'views/product_views.xml',
        'views/res_config_settings.xml',
        'views/res_city_views.xml',
        'views/account_move.xml',
        'views/intrastat_product_declaration.xml',
        'views/intrastat_product.xml'
    ],
    "pre_init_hook": 'pre_init_hook',
    'installable': True,
}
