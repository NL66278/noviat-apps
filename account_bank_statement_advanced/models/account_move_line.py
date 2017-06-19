# -*- coding: utf-8 -*-
# Copyright 2009-2017 Noviat.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models, _
from openerp.exceptions import Warning as UserError


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    move_state = fields.Selection(
        related='move_id.state', string='Move State',
        readonly=True)

    @api.onchange('tax_code_id')
    def _onchange_tax_code_id(self):
        if self.tax_code_id:
            self.tax_amount = self.debit or self.credit or False
        else:
            self.tax_amount = False

