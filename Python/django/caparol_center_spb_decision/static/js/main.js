document.addEventListener('DOMContentLoaded', () => {

    // Interiors

    var menuInteriors = document.querySelector('.menu_interiors'),
        menuLinkInteriors = document.querySelector('.menu__link_interiors'),
        menuKitchen = document.querySelector('.menu_kitchen'),
        menuItemKitchen = document.querySelector('.menu__item_kitchen');

    menuLinkInteriors.addEventListener('click', () => {
        menuLinkInteriors.style.color = 'purple';
        menuInteriors.style.display = 'flex';
        if (menuLinkInteriors.classList.contains('active')) {
            menuLinkInteriors.classList.remove('active');
            menuInteriors.style.display = 'none';
            menuKitchen.style.display = 'none';
        } else menuLinkInteriors.classList.add('active');
    });

    menuItemKitchen.addEventListener('click', () => {
        menuKitchen.style.display = 'flex';
        if (menuItemKitchen.classList.contains('active')) {
            menuItemKitchen.classList.remove('active');
            menuKitchen.style.display = 'none';
        } else menuItemKitchen.classList.add('active');
    });

});