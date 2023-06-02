# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.release import version_info

class ResCompany(models.Model):
    _inherit = "res.company"

    certificador_fel_sv = fields.Selection([], 'Certificador FEL SV')
