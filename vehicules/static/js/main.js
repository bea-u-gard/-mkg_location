// Menu responsive code JS
var menu_toggle = document.querySelector('.menu_toggle');
var navbar_container = document.querySelector('.navbar-container');
var nav_links = document.querySelectorAll('.navbar a'); // Sélectionne tous les liens du menu

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
const offreItems = document.querySelectorAll('.offre-item');

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, {
    threshold: 0.1 // Déclenche l'animation lorsque 10% de l'élément est visible
});

offreItems.forEach((item) => {
    observer.observe(item);
});

// Sélectionnez le header
const header = document.querySelector('header.section');

// Définissez la distance de défilement à partir de laquelle le header devient fixe
const scrollThreshold = 100; // Vous pouvez ajuster cette valeur

// Fonction pour gérer le défilement
window.addEventListener('scroll', () => {
    if (window.scrollY > scrollThreshold) {
        header.classList.add('fixed');
    } else {
        header.classList.remove('fixed');
    }
});

// // Récupérer les éléments
// const modal = document.getElementById("contractModal");
// const btn = document.getElementById("openContractBtn");
// const downloadBtn = document.getElementById("downloadContractBtn");
// const span = document.getElementsByClassName("close")[0];
// const acceptCheckbox = document.getElementById("acceptCheckbox");
// const acceptBtn = document.getElementById("acceptContractBtn");

// // Ouvrir le modal quand on clique sur le bouton
// btn.onclick = function() {
//     modal.style.display = "block";
// }

// // Télécharger le contrat
// downloadBtn.onclick = function() {
//     const link = document.createElement("a");
//     link.href = "/assets/contrat-location.pdf";  // Remplacez par le chemin de votre fichier PDF
//     link.download = "contrat-location.pdf";
//     link.click();
// }

// // Fermer le modal quand on clique sur la croix
// span.onclick = function() {
//     modal.style.display = "none";
// }

// // Fermer le modal quand on clique en dehors du modal
// window.onclick = function(event) {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }

// // Activer le bouton Accepter quand la checkbox est cochée
// acceptCheckbox.onchange = function() {
//     acceptBtn.disabled = !this.checked;
// }

// // Action quand on clique sur Accepter
// acceptBtn.onclick = function() {
//     alert("Vous avez accepté les conditions d'utilisation.");
//     modal.style.display = "none";
// }