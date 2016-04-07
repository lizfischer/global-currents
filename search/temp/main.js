$(document).ready(function(){
    $('.result-wrap a').hover(function() {
        delay(2000);
        $(this).siblings('.result-data').show();
    }, function(){
        $(this).siblings('.result-data').hide();
    });
});
