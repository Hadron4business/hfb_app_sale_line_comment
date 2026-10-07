// Hadron for Business sp. z o.o. - OPL-1
// Saves the comment typed in the website cart. Plain script (no imports) so it
// works the same in every Odoo version; keepalive lets the last request finish
// when the shopper clicks "Checkout" right after typing.
(function () {
    "use strict";
    const timers = {};

    function save(input) {
        const lineId = input.dataset.lineId;
        clearTimeout(timers[lineId]);
        fetch("/shop/cart/line_comment", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            keepalive: true,
            body: JSON.stringify({
                jsonrpc: "2.0",
                method: "call",
                params: { line_id: lineId, comment: input.value },
            }),
        });
    }

    document.addEventListener("input", (ev) => {
        const input = ev.target.closest && ev.target.closest(".o_hfb_line_comment_input");
        if (input) {
            clearTimeout(timers[input.dataset.lineId]);
            timers[input.dataset.lineId] = setTimeout(() => save(input), 600);
        }
    });
    document.addEventListener("change", (ev) => {
        const input = ev.target.closest && ev.target.closest(".o_hfb_line_comment_input");
        if (input) {
            save(input);
        }
    });
})();
