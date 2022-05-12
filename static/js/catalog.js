
$(document).ready(function () {
    $("#search-box").keypress(function(event) {
            if (event.keyCode === 13) {
                $("#search-btn").click();
            }
        });
    $("#search-btn").on('click', function(e) {
        e.preventDefault();
        let searchText = $("#search-box").val();
        $.ajax( {
            url: '/catalog?search_filter=' + searchText,
            type: 'GET',
            success: function(response) {
                let newHtml = response.data.map(d => {
                    return `<div class="well item">
                                <a class="single_item" href="/catalog/${d.id}">
                                    <img class="item-img" src="/media/${ d.image }" alt="${ d.name }" />
                                    <h4>${d.name}</h4>
                                </a>
                            </div>`
                });
                if (newHtml == '') {

                    $('.content').html("<h3>Sorry! No results found. </h3>")
                }
                else {

                    $('.content').html(newHtml.join(''));

                }
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
    $('#order-by').on("change", function(e) {

        let order_option = $('#order-by').find(":selected").attr("value");
        console.log(order_option)
        url = window.location.href
        if(url.indexOf('?') > -1) {
            url += '&order_by='
        }
        else{
            url += '?order_by='
        }

        $.ajax( {
            url: url + order_option,
            type: 'GET',
            success: function(response) {
                let newHtml = response.data.map(d => {
                    return `<div class="well item">
                                <a class="single_item" href="/catalog/${d.id}">
                                <div class="flex-grow-1">
                                    <img class="item-img" src="/media/${ d.image }" alt="${ d.name }" />
                                </div>
                                <div class="flex-shrink-0">
                                    <h3>${d.name}</h3>
                                    <p>Buyout price: ${ d.buyout.toFixed(2)  }</p>
                                </a>
                            </div>`

                });
                if (newHtml == '') {

                    $('.content').html("<h3>Sorry! No results found. </h3>")
                }
                else {

                    $('.content').html(newHtml.join(''));

                }
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    })
});

function reloadPage()
{
location.reload();
}



