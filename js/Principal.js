var btnAbrirPopUp = document.getElementById('RegistroVacuna'),
    overlay = document.getElementById('overlay'),
    popup = document.getElementById('popup'),
    btnCerraPopup = document.getElementById('btn-cerrar-popup');

btnAbrirPopUp.addEventListener('click', () => {
    overlay.classList.add('active');
    popup.classList.add('active');
});

btnCerraPopup.addEventListener('click', () => {
    overlay.classList.remove('active');
    popup.classList.remove('active');
});