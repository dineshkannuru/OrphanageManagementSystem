$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
    $(this).toggleClass('active');
    });
    
});

function sidebar_shift(class_name){
    $(".sidebar-active").removeClass("sidebar-active");
    $("."+class_name).addClass("sidebar-active");
}
