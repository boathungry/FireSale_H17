$(document).ready(function () {
    $("#search-btn").on('click', function(e) {
        e.preventDefault();
        let searchText = $("#search-box").val();
        $.ajax( {
            url: '/catalog?search_filter=' + searchText,
            type: 'GET',
            success: function(response) {
                let newHtml = response.data.map(d => {
                    return `<div class="well item">
                                <a href="/catalog/${d.id}">
                                    <img class="item-img" src="${d.image}" alt="${d.name}"/>
                                    <h4>${d.name}></h4>
                                    <div>${d.description}</div>
                                </a>
                            </div>`
                });
                $('.items').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});