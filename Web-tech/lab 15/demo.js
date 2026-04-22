$(function() {
    let sldr = $('.sldr'),
    slideWidth = $('.sl_ctr').outerWidth(),
    slideCount = $('.sldr img').length,
    prv_b = $('.prv_b'),
    nxt_b = $('.nxt_b'),
    margin = -slideWidth,
    interval;

    $('.sldr img:last').clone().prependTo('.sldr');
    $('.sldr img').eq(1).clone().appendTo('.sldr');
    $('.sldr').css('margin-left', -slideWidth);

    function animate() {
        margin -= slideWidth;
        if (margin <= -(slideCount * slideWidth)) {
            margin = -slideWidth;
            sldr.css({'marginLeft': margin});
        }
        sldr.animate({'marginLeft': margin}, 500);
    }

    function start() {
        interval = setInterval(animate, 3000);
    }

    function stop() {
        clearInterval(interval);
    }

    nxt_b.click(animate);
    prv_b.click(function(){
        margin += slideWidth * 2;
        animate();
    });

    sldr.hover(stop, start);
    start();
});

const track = document.querySelector('.slider-track');
const slides = Array.from(track.children);
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');

let currentIndex = 0;

function updateSlidePosition() {
    const width = slides[0].getBoundingClientRect().width;
    track.style.transform = `translateX(-${currentIndex * width}px)`;
}

nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % slides.length;
    updateSlidePosition();
});

prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateSlidePosition();
});

window.addEventListener('resize', updateSlidePosition);