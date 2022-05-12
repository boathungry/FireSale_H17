const show_rating_btn = document.getElementById("rating-btn");
const account_info_div = document.getElementById("account-info");
const star_dark_img = "../../static/images/star_dark.png"
const star_light_img = "../../static/images/star_light.png"

let rating = 0;

show_rating_btn.addEventListener("click", show_rating);

function show_rating() {
    //Create a container to hold all the rating stuff
    let rating_container = document.createElement("div");
    rating_container.id = "rating-container";
    account_info_div.appendChild(rating_container);
    //Show stars and add event listeners to them
    let star_div = document.createElement("div");
    star_div.id = "star-div";
    rating_container.appendChild(star_div);
    for (let i = 1; i <= 5; i++) {
        let star = document.createElement("img");
        star.src = star_light_img;
        star.id = "star-" + i.toString();
        star.className = "rating-star";
        star.addEventListener("mouseover", stars_darken);
        star.addEventListener("mouseleave", stars_lighten);
        star.addEventListener("click", stars_freeze);
        star_div.appendChild(star);
    }
    //Add a text box for the user to type in their review
    let review_div = document.createElement("div");
    review_div.id = "review-div";
    rating_container.appendChild(review_div);
    let review_box_label = document.createElement("label");
    review_box_label.id = "review-label";
    review_box_label.innerText = "Leave a review:";
    let review_box = document.createElement("textarea");
    review_box.id = "review-input";
    review_box.type = "text";
    review_div.appendChild(review_box_label);
    review_div.appendChild(review_box);
    //Make changes to the 'Rate user' button so it becomes a 'Cancel' button
    show_rating_btn.removeEventListener("click", show_rating);
    show_rating_btn.addEventListener("click", hide_rating);
    show_rating_btn.innerText = "Cancel";
}

function hide_rating() {
    let rating_container = document.getElementById("rating-container");
    rating_container.remove();
    show_rating_btn.removeEventListener("click", hide_rating);
    show_rating_btn.addEventListener("click", show_rating);
    show_rating_btn.innerText = "Rate user";
}

function get_prev_stars(star_id) {
    let stars = Array();
    for (let i = 1; i < parseInt(star_id) ; i++) {
        let star = document.getElementById("star-" + i.toString());
        stars.push(star);
    }
    return stars;
}

function get_next_stars(star_id) {
    let stars = Array();
    for (let i = 5; i > parseInt(star_id) ; i--) {
        let star = document.getElementById("star-" + i.toString());
        stars.push(star);
    }
    return stars;
}

function stars_darken() {
    this.src = star_dark_img;
    let star_id = this.id.slice(-1);
    let prev_stars = get_prev_stars(star_id);
    for (let i = 0; i < prev_stars.length ; i++) {
        let star = prev_stars[i];
        star.src = star_dark_img;
    }
}

function stars_lighten() {
    this.src = star_light_img;
    let star_id = this.id.slice(-1);
    let prev_stars = get_prev_stars(star_id);
    for (let i = 0; i < prev_stars.length ; i++) {
        let star = prev_stars[i];
        star.src = star_light_img;
    }
}

function single_star_darken(star) {
    star.src = star_dark_img;
}

function single_star_lighten(star) {
    star.src = star_light_img;
}

function stars_freeze() {
    //Lock in the appropriate colors on the stars
    rating = parseInt(this.id.slice(-1));
    let stars = document.getElementsByClassName("rating-star");
    for (let i = 0; i < stars.length; i++) {
        stars[i].removeEventListener("mouseover", stars_darken);
        stars[i].removeEventListener("mouseleave", stars_lighten);
        if (i >= rating) {
            single_star_lighten(stars[i]);
        }
        else {
            single_star_darken(stars[i]);
        }
    }
    //Add a button to confirm the rating, if it doesn't already exist
    if (document.getElementById("confirm-rating-btn") === null) {
        let rate_btn = document.createElement("button");
        rate_btn.type = "button";
        rate_btn.id = "confirm-rating-btn";
        rate_btn.className = "btn btn-primary";
        rate_btn.innerText = "Post review";
        rate_btn.addEventListener("click", confirm_rating)
        let rating_container = document.getElementById("rating-container");
        rating_container.appendChild(rate_btn);
    }
}

function confirm_rating() {
    let review = document.getElementById("review-input");
    let request = new XMLHttpRequest(); //create a http request
    request.open("POST", '../../User/' + userid + '/rate', true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('x-CSRFToken', csrf); //send the csrf token
    request.send(JSON.stringify({'rating': rating, 'review': review.value})); //send the rating and review with the request
    request.addEventListener("loadend", refresh_page)
}

function refresh_page() {
    window.location.reload()
}