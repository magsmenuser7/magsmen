$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        items:1,
        autoplay:true,
        autoplayTimeout: 5000,
        loop:true,
        nav:false,
        dots:false,
        responsiveClass: true,
        responsive:{
            0:{
                items: 1,
                
            },
            600:{
                items: 3,
               
            },
            1000:{
                items: 1,
            }
        }
    });
});

