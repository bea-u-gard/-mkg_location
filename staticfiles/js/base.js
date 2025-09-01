// Menu responsive code JS
var menu_toggle = document.querySelector('.menu_toggle');
var navbar_container = document.querySelector('.navbar-container');
var nav_links = document.querySelectorAll('.navbar a');

// Ouvrir/fermer le menu
menu_toggle.onclick = function() {
    menu_toggle.classList.toggle('active');
    navbar_container.classList.toggle('responsive');
}

// Fermer le menu lorsqu'un lien est cliqué
nav_links.forEach(function(link) {
    link.addEventListener('click', function() {
        menu_toggle.classList.remove('active');
        navbar_container.classList.remove('responsive');
    });
});

// Animation au scroll avec Intersection Observer
const header = document.querySelector('header.section');
const scrollThreshold = 100;

window.addEventListener('scroll', () => {
    if (window.scrollY > scrollThreshold) {
        header.classList.add('fixed');
    } else {
        header.classList.remove('fixed');
    }
});