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

	Customer Comment per Order Line - stock moves
	Shows the current customer comment of the sales order line on the delivery
	order and adds it to the move description printed on the delivery slip.
"""
from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_line_comment = fields.Text(
        related='sale_line_id.line_comment', string="Customer Comment")

    @api.depends('sale_line_id.line_comment')
    def _compute_description_picking(self):
        # Odoo builds the move description from the sales order line; the
        # comment is added on its own line, so it is printed on the delivery slip.
        super()._compute_description_picking()
        for move in self:
            comment = move.sale_line_id.line_comment
            if comment and not move.description_picking_manual:
                move.description_picking = '%s\n%s' % (move.description_picking or '', comment)

#EoF
