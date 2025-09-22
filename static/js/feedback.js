document.addEventListener("DOMContentLoaded", function () {
    // Star Rating System
    const stars = document.querySelectorAll('.star');
    const ratingInput = document.getElementById('rating');

    stars.forEach((star, index) => {
        star.addEventListener('click', () => {
            const value = index + 1;
            ratingInput.value = value;

            stars.forEach((s, i) => {
                if (i < value) {
                    s.classList.remove('fa-regular');
                    s.classList.add('fa-solid');
                } else {
                    s.classList.remove('fa-solid');
                    s.classList.add('fa-regular');
                }
            });
        });
    });

    // Navbar Scroll Active Link Highlight
    const links = document.querySelectorAll('.navbar-nav .nav-link');
    window.addEventListener('scroll', () => {
        let fromTop = window.scrollY + 110;

        links.forEach(link => {
            let section = document.querySelector(link.getAttribute('href'));
            if (section && section.offsetTop <= fromTop && section.offsetTop + section.offsetHeight > fromTop) {
                links.forEach(l => {
                    l.style.fontWeight = 'normal';
                    l.style.color = '#000';
                    l.style.borderBottom = 'none';
                });

                link.style.fontWeight = 'bold';
                link.style.color = '#0d6efd';
                link.style.borderBottom = '2px solid #0d6efd';
            }
        });
    });

    // Owl Carousel Initialization
    if (typeof jQuery !== 'undefined' && typeof jQuery.fn.owlCarousel !== 'undefined') {
        $('.owl-carousel').owlCarousel({
            loop: true,
            margin: 10,
            nav: true,
            dots: true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                1000: {
                    items: 3
                }
            }
        });
    }
});

