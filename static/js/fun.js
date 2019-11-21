$(function ()
{
    $("#term_name").change(function () {
        var term_name = $('#term_name').val();
        $.get('/get_week_ord/',{'term_name': term_name}, function(ret){
            $("#week_ord option").remove()
            $.each(ret, function (n, value) {
                $("#week_ord").append("<option value=" + value + ">第" + n + "周</option>");
            })
        });
    });




});
