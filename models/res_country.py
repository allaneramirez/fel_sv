# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class Country(models.Model):
    _inherit = 'res.country'

    codigo_fel_sv = fields.Char('Código FEL SV')
