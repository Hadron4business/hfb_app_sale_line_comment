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

	Customer Comment per Order Line - products
	Switch and label of the cart comment box, on the product and on the product
	category (inherited by subcategories); helpers resolving whether a product
	asks for a comment and with which label.
"""
from odoo import _, fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    sale_line_comment = fields.Boolean(
        string="Ask for a Comment in the Cart",
        help="Products of this category and of its subcategories get a comment box in the website cart.")
    sale_line_comment_label = fields.Char(
        string="Comment Label", translate=True,
        help="Label of the comment box, e.g. 'Engraving text'. Default: 'Comment'.")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sale_line_comment = fields.Boolean(
        string="Ask for a Comment in the Cart",
        help="Shows a comment box next to this product in the website cart. "
             "Can also be switched on for a whole product category.")
    sale_line_comment_label = fields.Char(
        string="Comment Label", translate=True,
        help="Label of the comment box, e.g. 'Engraving text'. "
             "Empty: the label of the category, otherwise 'Comment'.")

    def _sale_line_comment_categories(self):
        """Product category and its parents, nearest first."""
        self.ensure_one()
        categ = self.categ_id
        categories = self.env['product.category']
        while categ:
            categories |= categ
            categ = categ.parent_id
        return categories

    def _sale_line_comment_enabled(self):
        self.ensure_one()
        return self.sale_line_comment or any(
            self._sale_line_comment_categories().mapped('sale_line_comment'))

    def _sale_line_comment_get_label(self):
        self.ensure_one()
        if self.sale_line_comment_label:
            return self.sale_line_comment_label
        for categ in self._sale_line_comment_categories():
            if categ.sale_line_comment and categ.sale_line_comment_label:
                return categ.sale_line_comment_label
        return _("Comment")

#EoF
