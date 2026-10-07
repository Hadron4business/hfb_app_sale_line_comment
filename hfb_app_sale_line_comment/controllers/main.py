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
"""	@version	17.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.07

	Customer Comment per Order Line - website
	JSON route saving the comment typed in the website cart on a line of the
	current cart, only for products that ask for a comment.
"""
from odoo import http
from odoo.http import request

MAX_COMMENT_LENGTH = 2000


class SaleLineCommentController(http.Controller):

    @http.route('/shop/cart/line_comment', type='json', auth='public', website=True, methods=['POST'])
    def cart_line_comment(self, line_id, comment, **kwargs):
        order = request.website.sale_get_order()
        if not order:
            return {'error': 'no_order'}
        line = order.order_line.filtered(lambda l: l.id == int(line_id))
        if not line or not line.product_template_id._sale_line_comment_enabled():
            return {'error': 'not_applicable'}
        comment = (comment or '').strip()[:MAX_COMMENT_LENGTH]
        line.sudo().line_comment = comment or False
        return {'success': True}

#EoF
