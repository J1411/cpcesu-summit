function pageify(){
    $('.dtBasicExample').DataTable({
        'pageLength': 25,
        'lengthMenu': [[10, 25, 50, 100, 500, 1000, -1], [10, 25, 50, 100, 500, 1000, "All"]],
        "dom": '<"top">r<"bottom"litp><"clear">'
    });
    $('.dataTables_length').addClass('bs-select');
    $('.dataTables_filter').addClass('pull-left');
    $('.dataTables_paginate').addClass('pull-left');
}
$(document).ready(function ()
{

$(document.getElementById("project")).addClass("tab-background")
$(document.getElementById("contentBody")).addClass("content-background");

    pageify();

    $('#select_all_1').click(function () {
        $('.export_list_1').prop("checked", !$('.export_list_1').prop("checked"));
        $('#select_all_1').prop("checked", $('.export_list_1').prop("checked"));
    });

    $('#select_all_2').click(function () {
        $('.export_list_2').prop("checked", !$('.export_list_2').prop("checked"));
        $('#select_all_1').prop("checked", $('.export_list_1').prop("checked"));
    });
});