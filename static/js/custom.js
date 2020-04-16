$(document).ready(function () {
    $(document).click(function (e) { 
        clickover = $(e.target);
        opened = $(".navbar-collapse").hasClass("show");
        if(opened && !clickover.hasClass("navbar-toggler")){
            $(".navbar-toggler").click();
        }        
    });
});