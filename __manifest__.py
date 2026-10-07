# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=0 shiftwidth=4 smarttab expandtab fileformat=unix
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
{
    'name': "Customer Comment per Order Line",
    'summary': "Let shoppers add a note to a product in the cart (engraving text, size, prescription number...) - "
               "it follows the line to the order, invoice and delivery",
    'description': """
Customer Comment per Order Line
===============================

Some products need one more piece of information from the customer: the
text to engrave, the name to print on a shirt, a prescription number, "no
onions". Odoo has no place for it on the cart line, so customers write it in
the checkout note (if at all) and somebody has to match it to the right
product by hand.

With this app you switch on a comment box for chosen products or whole
product categories, with your own label ("Engraving text"). The shopper fills
it in next to the product in the cart, and the comment travels with that
line:

* sales order line (also editable in the backend),
* customer portal and printed quotation / order,
* invoice line and printed invoice,
* delivery order (in the description of the move, so it is printed on the
  delivery slip as well).
""",
    'version': "18.0.1.0.0",
    'author': "Hadron for Business sp. z o.o.",
    'website': "http://hadronforbusiness.com",
    'license': "OPL-1",
    'category': "Website/eCommerce",
    'depends': [
        'website_sale',
        'sale_stock',
    ],
    'data': [
        'views/product_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/stock_picking_views.xml',
        'views/website_sale_templates.xml',
        'views/report_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'hfb_app_sale_line_comment/static/src/js/cart_line_comment.js',
        ],
    },
    'images': [
        'static/description/banner_screenshot.png',
    ],
    'installable': True,
    'application': False,
}
