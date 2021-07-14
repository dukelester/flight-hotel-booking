$(document).ready(function() {
    //Get data from server url and add them to the list attribute
    $.getJSON('/flightsearch', function(data) {
        $.each(data, function(key, value) {
            $("#datalist-data").append(`<option class="px-3 py-2 border-b border-gray-200" value="${value.cityname}">`);
        });
    });
});