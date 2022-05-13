const offer_button = document.getElementById("make-offer-btn");
const offer_input = document.getElementById("make-offer-input");

offer_button.addEventListener("click", function () {
    let amount = offer_input.value;
    if (window.confirm('You are making an offer of $' + amount + ' for this item.')) {
        let request = new XMLHttpRequest(); //create a http request
        request.open("POST", '../../offer/make_offer/' + itemid, true);
        request.setRequestHeader('Content-Type', 'application/json');
        request.setRequestHeader('x-CSRFToken', csrf); //send the csrf token
        request.addEventListener("loadend", refresh_page) //refresh the page once the request has been successfully sent
        request.send(JSON.stringify({'amount': amount}));
    }
});

/**
 * @name refresh_page
 * @description Refreshes the page.
 *
 */
function refresh_page() {
    window.location.reload()
}