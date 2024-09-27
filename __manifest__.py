# -*- encoding: utf-8 -*-

{
    'name': 'FEL El Salvador',
    'version': '1.0',
    'category': 'Custom',
    'description': """ Campos y funciones base para la facturación electrónica en El Salvador """,
    'author': 'aquíH',
    'website': 'http://aquih.com/',
    'depends': ['l10n_sv'],
    'data': [
        'views/account_view.xml',
        'views/res_company_view.xml',
        'views/partner_view.xml',
        'views/report_invoice.xml',
    ],
    'demo': [],
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
