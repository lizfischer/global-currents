$(document).ready(function(){
    $('.result-wrap a').hover(function() {
        $(this).siblings('.result-data').delay(1000).show();
    }, function(){
        $(this).siblings('.result-data').hide();
    });
});
