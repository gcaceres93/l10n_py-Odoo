# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 Cubic ERP - Teradata SAC. (http://cubicerp.com)

{
    'name': 'Paraguay - Accounting',
    'version': '2.0',
    'description': """
Plan de cuentas paraguayo y localizacion de impuestos.
==================================================

Plan contable paraguayo e impuestos de acuerdo a disposiciones vigentes.

Desarrollado por RAPIDSOFT.

http://www.rapidsoft.com.py

Para utilizar la localización, también deberá descargar el modulo account_parent: http://www.odoo.com/apps/modules/10.0/account_parent/

Para más información, contactarnos en info@rapidsoft.com.py

    """,
    'author': ['Rapidsoft'],
    'website': 'http://www.rapidsoft.com.py',
    'category': 'Localization',
    'depends': ['base', 'account','account_parent'],
    'data':[
        'data/l10n_py_chart_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.yml',
    ],
}
