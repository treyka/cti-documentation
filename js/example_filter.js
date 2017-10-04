function filter_idiom_table(by_tag) {
    if (by_tag === "None") {
        $("#examples-table > tbody > tr").show();
    } else {
        $("#examples-table > tbody > tr:has('img[data-tag=\"" + by_tag + "\"]')").show();
        $("#examples-table > tbody > tr:not(:has('img[data-tag=\"" + by_tag + "\"]'))").hide();
    }
}

$(document).ready(function() {
    $("#tag-filterer > li > a.tag-filter").click(function() {
        var label = this.textContent.trim();
        filter_idiom_table(label);
    })
    
    var idiom_table = $("#examples-table");
    var rows = $(idiom_table).find('tbody > tr').get();
    $.each(rows, function(index, row) {
        $(idiom_table).children('tbody').append(row);
    });
    
    if (window.location.hash) {
        filter_idiom_table(window.location.hash.substring(1));
    }
});