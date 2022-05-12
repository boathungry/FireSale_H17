const show_rating_btn = document.getElementById("rating-btn");
const account_info_div = document.getElementById("account-info");

show_rating_btn.addEventListener("click", show_rating);

function show_rating() {
    let star_div = document.createElement("div");
    star_div.id = "star-div";
    account_info_div.appendChild(star_div);
    for (let i = 1; i <= 5; i++) {
        let star = document.createElement("img");
        star.src = "../../static/images/star_light.png";
        star.id = "star-" + i.toString();
        star.className = "rating-star";
        star.addEventListener("mouseover", star_turn_dark);
        star.addEventListener("mouseleave", star_turn_light);
        star.addEventListener("click", star_freeze);
        star_div.appendChild(star);
    }
}

function get_prev_stars(star_id) {
    let stars = Array();
    for (let i = 1; i < parseInt(star_id) ; i++) {
        let star = document.getElementById("star-" + i.toString());
        stars.push(star);
    }
    return stars
}

function star_turn_dark() {
    this.src = "../../static/images/star_dark.png";
    let star_id = this.id.slice(-1);
    let prev_stars = get_prev_stars(star_id);
    for (let i = 0; i < prev_stars.length ; i++) {
        let star = prev_stars[i];
        star.src = "../../static/images/star_dark.png";
    }
}

function star_turn_light() {
    this.src = "../../static/images/star_light.png";
    let star_id = this.id.slice(-1);
    let prev_stars = get_prev_stars(star_id);
    for (let i = 0; i < prev_stars.length ; i++) {
        let star = prev_stars[i];
        star.src = "../../static/images/star_light.png";
    }
}

function star_freeze() {
    this.removeEventListener("mouseover", star_turn_dark);
    this.removeEventListener("mouseleave", star_turn_light);
    let star_id = this.id.slice(-1);
    let prev_stars = get_prev_stars(star_id);
    for (let i = 0; i < prev_stars.length ; i++) {
        let star = prev_stars[i];
        star.removeEventListener("mouseover", star_turn_dark);
        star.removeEventListener("mouseleave", star_turn_light);
    }
    let rate_btn = document.createElement("a");
    rate_btn.id = "rate-btn";
    rate_btn.className = "btn btn-primary";
    rate_btn.href = "#";
    rate_btn.innerHTML = "Confirm rating"
    let star_div = document.getElementById("star-div");
    //add button to star div, etc
}

function restore_event_listeners() {
    this.addEventListener("mouseover", star_turn_dark);
    this.addEventListener("mouseleave", star_turn_light);
}