const offer_button = document.getElementById("make-offer-btn");
const offer_input = document.getElementById("make-offer-input");

offer_button.addEventListener("click", function () {
    let amount = offer_input.value;
    if (window.confirm('You are making an offer of $' + amount + ' for this item.')) {
        console.log("yes")
    }
    else {
        console.log("no")
    };
});