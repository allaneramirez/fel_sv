# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from .select_options import DEPARTAMENTOS_SELECTION
import logging

class Partner(models.Model):
    _inherit = "res.partner"

    # nombre_facturacion_fel_sv = fields.Char('Nombre Facturación FEL SV')
    descripcion_actividad = fields.Char('Descripcion de Actividad Economina')
    nombre_comercial = fields.Char('Nombre Comercial Fel')
    codigo_pais =  fields.Char('Codigo del Pais de Exportación')
    tipo_persona = fields.Selection([('1','Persona Natural'),('2','Persona Juridica')])
    vat = fields.Char(string='NIT/DUI')
    # nit_facturacion_fel_sv = fields.Char('NIT Facturación FEL SV')
    # tipo_documento_fel_sv = fields.Char('Tipo de Documento FEL SV')
    departamento_fel_sv = fields.Selection(DEPARTAMENTOS_SELECTION,'Código Departamente FEL SV')
    municipio_fel_sv = fields.Char('Código de Municipio facturación FEL SV')
    exento_iva = fields.Boolean("Es Exento de IVA")
    tipo_documento_fel = fields.Selection(
        selection=[
            ('36', 'NIT'),
            ('13', 'DUI'),
            ('37', 'Otro'),
            ('03', 'Pasaporte'),
            ('02', 'Carnet de Residente'),
        ],
        string='Tipo de Documento',
        required=True,
    )