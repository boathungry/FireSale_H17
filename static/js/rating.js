const show_rating_btn = document.getElementById("rating-btn");
const account_info_div = document.getElementById("account-info");
const star_dark_img = "../../static/images/star_dark.png"
const star_light_img = "../../static/images/star_light.png"

let rating = 0;

show_rating_btn.addEventListener("click", show_rating);

function show_rating() {
    let star_div = document.createElement("div");
    star_div.id = "star-div";
    account_info_div.appendChild(star_div);
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
    show_rating_btn.removeEventListener("click", show_rating);
    show_rating_btn.addEventListener("click", hide_rating);
    show_rating_btn.innerText = "Cancel";
}

function hide_rating() {
    let star_div = document.getElementById("star-div");
    star_div.remove();
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
    if (document.getElementById("rate-btn") === null) {
        let rate_btn = document.createElement("a");
        rate_btn.id = "rate-btn";
        rate_btn.className = "btn btn-primary";
        rate_btn.href = "#";
        rate_btn.innerText = "Confirm rating";
        let star_div = document.getElementById("star-div");
        star_div.appendChild(rate_btn);
    }
}

function restore_event_listeners() {
    this.addEventListener("mouseover", stars_darken);
    this.addEventListener("mouseleave", stars_lighten);
}