// JavaScript for navigation toggle
document.addEventListener('DOMContentLoaded', function () {
    var navbar = document.querySelector('.navbar');

    var navbarToggler = document.querySelector('.navbar-toggler');
    navbarToggler.addEventListener('click', function () {
        navbar.classList.toggle('show');
    });

    var today = new Date().toISOString().split('T')[0];
    $('input[name="due_date"]').attr('min', today);
});


// prevent booking of past dates
