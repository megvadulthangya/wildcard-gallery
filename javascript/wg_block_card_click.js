/* Block the native cardClicked handler on Wildcard Gallery cards
   in the Extra Networks tab so clicking a card never auto-inserts
   the activation text into the prompt.

   Works by adding a *capturing* listener on the cards container;
   capture-phase runs before the inline onclick on the child <div>,
   so stopPropagation() prevents the event from ever reaching it. */

(function () {
    function blockNativeClick(containerId) {
        var container = gradioApp().getElementById(containerId);
        if (!container) return;
        container.addEventListener('click', function (e) {
            var card = e.target.closest('.card, .wg-card');
            if (card) {
                e.stopPropagation();
                e.preventDefault();
            }
        }, true);   // ← capture phase
    }

    onUiLoaded(function () {
        blockNativeClick('txt2img_wildcards_cards_html');
        blockNativeClick('img2img_wildcards_cards_html');
    });
})();
