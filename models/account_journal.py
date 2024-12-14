from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountJournal(models.Model):
    _inherit = "account.journal"

    generar_fel_sv = fields.Boolean('Generar FEL SV')
    tipo_documento_fel_sv = fields.Selection([('1', 'Factura'), ('3', 'Comprobante de crédito fiscal'), ('4', 'Nota de remisión'), ('5', 'Nota de crédito'), ('6', 'Nota de débito'), ('7', 'Comprobante de retención'), ('8', 'Comprobante de liquidación'), ('9', 'Documento contable de liquidación'), ('11', 'Facturas de exportación'), ('14', 'Factura de sujeto excluido'), ('15', 'Comprobante de donación')], 'Tipo de Documento FEL SV', copy=False)
    condicion_pago_fel_sv = fields.Selection([('1', 'Contado'), ('2', 'Crédito'), ('3', 'Otro')], 'Condicion de Pago por Defecto FEL SV')
    forma_pago_fel_sv = fields.Selection([('01', 'Billetes y monedas'), ('02', 'Tarjeta Débito'), ('03', 'Tarjeta Crédito')], 'Forma de Pago por Defecto FEL SV')
    # codigo_establecimiento_sv = fields.Char('Código Establecimiento FEL SV')
    error_en_historial_fel_sv = fields.Boolean('Error FEL SV en historial', help='Los errores no se muestran en pantalla, solo se registran en el historial')
    # enviar_lineas_en_cero_fel_sv = fields.Boolean('Enviar lineas en cero para FEL SV')
    sequence_id = fields.Many2one(
        'ir.sequence',
        string="Secuencia Numero Control Fel",
        domain="[('name', 'ilike', 'FEL')]",
        help="Secuencia usada para generar números únicos segun tipo DTE"
    )
