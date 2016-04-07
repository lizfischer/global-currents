$(document).ready(function(){
    $('.result-wrap img').click(function() {
        $(this).siblings('.result-data').fadeIn(300).delay(1000).fadeOut(300);
    });
});
