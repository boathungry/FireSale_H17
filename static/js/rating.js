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
        star.addEventListener("mouseover", star_hover);
        star.addEventListener("mouseleave", star_hover_end);
        star.addEventListener("click", star_click);
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

function star_hover() {
    this.src = "../../static/images/star_dark.png";
    let star_id = this.id.slice(-1);
    let prev_stars = get_prev_stars(star_id);
    for (let i = 0; i < prev_stars.length ; i++) {
        let star = prev_stars[i];
        star.src = "../../static/images/star_dark.png";
    }
}

function star_hover_end() {
    this.src = "../../static/images/star_light.png";
    let star_id = this.id.slice(-1);
    let prev_stars = get_prev_stars(star_id);
    for (let i = 0; i < prev_stars.length ; i++) {
        let star = prev_stars[i];
        star.src = "../../static/images/star_light.png";
    }
}

function star_click() {
    this.removeEventListener("mouseover", star_hover);
    this.removeEventListener("mouseleave", star_hover_end);
    let star_id = this.id.slice(-1);
    let prev_stars = get_prev_stars(star_id);
    for (let i = 0; i < prev_stars.length ; i++) {
        let star = prev_stars[i];
        star.removeEventListener("mouseover", star_hover);
        star.removeEventListener("mouseleave", star_hover_end);
    }
}