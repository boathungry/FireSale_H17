const offer_button = document.getElementById("make-offer-btn");
const offer_input = document.getElementById("make-offer-input");

offer_button.addEventListener("click", function () {
    let amount = offer_input.value;
    if (window.confirm('You are making an offer of $' + amount + ' for this item.')) {
        let request = new XMLHttpRequest(); //create a http request
        request.open("POST", '../../offer/make_offer/' + itemid, true);
        request.setRequestHeader('Content-Type', 'application/json');
        request.setRequestHeader('x-CSRFToken', csrf); //send the csrf token
        request.send(JSON.stringify({'amount':amount})); //send the offer amount with the request
    };
});