# Customer Comment per Order Line

Switch on a comment box for chosen products or whole categories, with your own label. The comment follows the order line everywhere.

## What it does

- **Per product or category** - Switch the box on for a single product or for a whole product category (subcategories included).
- **Your own label** - "Engraving text", "Name on the shirt", "Prescription number" - translatable into every website language.
- **Saved as you type** - No extra button: the comment is stored on the cart line while the shopper types.
- **Sales order and portal** - Visible and editable on the order line in the backend, shown to the customer in the portal and on the printed quotation/order.
- **Invoice** - Copied to the invoice line and printed on the invoice.
- **Delivery** - Added to the description of the delivery move, so the warehouse sees it on the transfer and on the delivery slip.

## How to use it

1. Open a product, tab Sales, section Extra Info: tick Ask for a Comment in the Cart and optionally set a Comment Label. Or do the same on a product category (Inventory/Sales > Configuration > Product Categories).
2. On the website, add the product to the cart: a comment box with your label appears under the product.
3. Confirm the order: the comment is on the order line (column Customer Comment), in the customer portal and on the printed order.
4. Create the invoice and validate the delivery: the comment is on the invoice line, on the printed invoice and on the delivery slip.

## Good to know

- The comment can also be typed or changed by your team on the order line in the backend.
- The invoice keeps a copy of the comment from the moment it was created; the delivery shows the comment from the moment the order was confirmed (and the live value in the transfer list).
- Comments are limited to 2000 characters.

## Technical

- Depends on `website_sale` and `sale_stock`.
- Fields: `sale.order.line.line_comment`, `account.move.line.line_comment`, `stock.move.sale_line_comment` (related).
- Website route `/shop/cart/line_comment` (JSON), plain JS without imports.
- Delivery: `stock.move._compute_description_picking` adds the comment on its own line of `description_picking`.

## Status

Odoo 19 build. Tested on the Odoo.sh test instances (automated RPC tests and manual tests, 2026-10-07). Missing before publication: icon, banner.
