$(document).ready(function(){
    //highlight when a nav clicked
    var $cols = $('.sidenav a').click(function(e) {
        $cols.removeClass('highlight');
        $(this).addClass('highlight');
    });
});