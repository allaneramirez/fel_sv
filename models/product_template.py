from odoo import models, fields, api, _

import logging


class ProductTemplate(models.Model):
    _inherit = "product.template"

    codigo_unidad_medida_fel_sv = fields.Char('Código Unidad de Medida FEL SV')
    numero_secuencial = fields.Char(
        string='Número Secuencial',
        readonly=True,
        copy=False,
    )
    tipo_venta = fields.Selection(
        [('1', 'Venta Gravada'),
         ('2', 'Venta No Sujeta'),
         ('3', 'Venta Exenta'),
         ('4', 'Venta No gravada')],
        default="1",
        string="Tipo de Venta Fel"
    )
    unidad_medida_fel = fields.Selection(
        selection=[
            ('1', 'Metro'),
            ('2', 'Yarda'),
            ('3', 'Vara'),
            ('4', 'Pie'),
            ('5', 'Pulgada'),
            ('6', 'Milímetro'),
            ('8', 'Milla cuadrada'),
            ('9', 'Kilómetro cuadrado'),
            ('10', 'Hectárea'),
            ('11', 'Manzana'),
            ('12', 'Acre'),
            ('13', 'Metro cuadrado'),
            ('14', 'Yarda cuadrada'),
            ('15', 'Vara cuadrada'),
            ('16', 'Pie cuadrado'),
            ('17', 'Pulgada cuadrada'),
            ('18', 'Metro cúbico'),
            ('19', 'Yarda cúbica'),
            ('20', 'Barril'),
            ('21', 'Pie cúbico'),
            ('22', 'Galón'),
            ('23', 'Litro'),
            ('24', 'Botella'),
            ('25', 'Pulgada cúbica'),
            ('26', 'Mililitro'),
            ('27', 'Onza fluida'),
            ('29', 'Tonelada métrica'),
            ('30', 'Tonelada'),
            ('31', 'Quintal métrico'),
            ('32', 'Quintal'),
            ('33', 'Arroba'),
            ('34', 'Kilogramo'),
            ('35', 'Libra troy'),
            ('36', 'Libra'),
            ('37', 'Onza troy'),
            ('38', 'Onza'),
            ('39', 'Gramo'),
            ('40', 'Miligramo'),
            ('42', 'Megawatt'),
            ('43', 'Kilowatt'),
            ('44', 'Watt'),
            ('45', 'Megavoltio-amperio'),
            ('46', 'Kilovoltio-amperio'),
            ('47', 'Voltio-amperio'),
            ('49', 'Gigawatt-hora'),
            ('50', 'Megawatt-hora'),
            ('51', 'Kilowatt-hora'),
            ('52', 'Watt-hora'),
            ('53', 'Kilovoltio'),
            ('54', 'Voltio'),
            ('55', 'Millar'),
            ('56', 'Medio millar'),
            ('57', 'Ciento'),
            ('58', 'Docena'),
            ('59', 'Unidad'),
            ('99', 'Otra'),
        ],
        string='Unidad de Medida FEL',
        default="59"  # Cambiar a False si no debe ser obligatorio
    )
