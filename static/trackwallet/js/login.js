document.addEventListener('DOMContentLoaded', () => {
    const passwordField = document.querySelector('#passwordField');
    const togglePassword = document.querySelector('#togglePassword');

    togglePassword.addEventListener('click', () => {
        const type = passwordField.getAttribute('type') === 'password' ? 'text': 'password';
        passwordField.setAttribute('type', type);
        togglePassword.classList.toggle('bi-eye');
    });
});

