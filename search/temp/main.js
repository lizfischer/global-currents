$(document).ready(function(){
    $('.result-wrap').hover(function() {
        $(this).children('.result-data').delay(3000).show();
    }, function(){
        $(this).children('.result-data').hide();
    });
});
