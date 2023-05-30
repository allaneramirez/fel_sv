# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class Partner(models.Model):
    _inherit = "res.partner"

    nombre_facturacion_fel_sv = fields.Char('Nombre Facturación FEL SV')
    nit_facturacion_fel_sv = fields.Char('NIT Facturación FEL SV')
    tipo_documento_fel_sv = fields.Char('Tipo de Documento FEL SV')
    departamento_fel_sv = fields.Char('Código Departamente FEL SV')
    municipio_fel_sv = fields.Char('Código de Municipio facturación FEL SV')