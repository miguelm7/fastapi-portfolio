document.addEventListener('DOMContentLoaded', () => {
    // Obtener todos los elementos con la clase "navbar-burger"
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Si hay elementos con la clase "navbar-burger"
    if ($navbarBurgers.length > 0) {
  
      $navbarBurgers.forEach(el => {
        el.addEventListener('click', () => {
  
          // Obtener el target desde el atributo "data-target"
          const target = el.dataset.target;
          const $target = document.getElementById(target);
  
          // Toggle entre las clases "is-active" en la hamburguesa y el menú
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
        });
      });
    }
  });
  