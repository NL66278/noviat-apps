# -*- coding: utf-8 -*-
# Copyright 2009-2017 Noviat.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def _default_intrastat_transaction(self):
        transaction = super(
            AccountInvoice, self)._default_intrastat_transaction()
        if not transaction:
            cpy_id = self.env[
                'res.company']._company_default_get('account.invoice')
            cpy = self.env['res.company'].browse(cpy_id)
            if cpy.country_id.code.lower() == 'be':
                module = __name__.split('addons.')[1].split('.')[0]
                transaction = self.env.ref(
                    '%s.intrastat_transaction_1' % module)
        return transaction
