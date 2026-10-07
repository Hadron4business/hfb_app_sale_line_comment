# -*- coding: utf-8 -*-
#################################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2017-2026 Hadron for Business sp. z o.o. (http://hadronforbusiness.com)
#
# This program is proprietary software, licensed under the Odoo Proprietary
# License v1.0 (OPL-1). Its use is governed by the Odoo Apps terms available
# at https://www.odoo.com/documentation/user/legal/licenses.html and the
# license agreement accepted at purchase / installation.
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the
# Software or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in
# all copies or substantial portions of the Software.
#
#################################################################################
"""	@version	19.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.07

	Customer Comment per Order Line - sales order lines
	Comment field on the sales order line, copied to the invoice line when
	invoicing.
"""
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line_comment = fields.Text(
        string="Customer Comment",
        help="Note entered by the customer for this product in the website cart. "
             "Copied to the invoice line and to the delivery.")

    def _prepare_invoice_line(self, **optional_values):
        vals = super()._prepare_invoice_line(**optional_values)
        if self.line_comment:
            vals['line_comment'] = self.line_comment
        return vals


#EoF
