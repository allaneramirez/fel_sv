# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.release import version_info

from lxml import etree
from datetime import datetime

import base64
import re
import json

import odoo.addons.l10n_gt_extra.a_letras as a_letras

#from OpenSSL import crypto
#import xmlsig
#from xades import XAdESContext, template, utils, ObjectIdentifier
#from xades.policy import GenericPolicyId, ImpliedPolicy

import logging
import re

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    firma_fel_sv = fields.Char('Firma FEL', copy=False)
    condicion_pago_fel_sv = fields.Selection([('1', 'Contado'), ('2', 'Crédito'), ('3', 'Otro')], 'Condicion de Pago FEL')
    motivo_fel_sv = fields.Char(string='Motivo FEL')
    documento_xml_fel_sv = fields.Binary('Documento XML FEL', copy=False)
    documento_xml_fel_sv_name = fields.Char('Nombre documento XML FEL', default='documento_xml_fel.xml', size=32)
    resultado_xml_fel_sv = fields.Binary('Resultado XML FEL', copy=False)
    resultado_xml_fel_sv_name = fields.Char('Nombre resultado XML FEL', default='resultado_xml_fel.xml', size=32)
    certificador_fel_sv = fields.Char('Certificador FEL', copy=False)

    def num_a_letras(self, amount):
        return a_letras.num_a_letras(amount,completo=True)

    def error_certificador(self, error):
        self.ensure_one()
        factura = self
        if factura.journal_id.error_en_historial_fel:
            factura.message_post(body='<p>No se publicó la factura por error del certificador FEL:</p> <p><strong>'+error+'</strong></p>')
        else:
            raise UserError('No se publicó la factura por error del certificador FEL: '+error)

    def requiere_certificacion(self, certificador=''):
        self.ensure_one()
        factura = self
        requiere = factura.is_invoice() and factura.journal_id.generar_fel_sv and factura.amount_total != 0
        if certificador:
            requiere = requiere and ( factura.company_id.certificador_fel_sv == certificador or not factura.company_id.certificador_fel_sv )
        return requiere

    def error_pre_validacion(self):
        self.ensure_one()
        factura = self
        if factura.firma_fel:
            factura.error_certificador("La factura ya fue validada, por lo que no puede ser validada nuevamente")
            return True

        return False

class AccountJournal(models.Model):
    _inherit = "account.journal"

    generar_fel_sv = fields.Boolean('Generar FEL')
    tipo_documento_fel_sv = fields.Selection([('1', 'Factura'), ('3', 'Comprobante de crédito fiscal'), ('4', 'Nota de remisión'), ('5', 'Nota de crédito'), ('6', 'Nota de débito'), ('7', 'Comprobante de retención'), ('8', 'Comprobante de liquidación'), ('9', 'Documento contable de liquidación'), ('11', 'Facturas de exportación'), ('14', 'Factura de sujeto excluido'), ('15', 'Comprobante de donación')], 'Tipo de Documento FEL', copy=False)
    error_en_historial_fel_sv = fields.Boolean('Error FEL en historial', help='Los errores no se muestran en pantalla, solo se registran en el historial')
    enviar_lineas_en_cero_fel_sv = fields.Boolean('Enviar lineas en cero para FEL')