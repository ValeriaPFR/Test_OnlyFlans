document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector("form.needs-validation");
    var password = document.getElementById("password");
    var confirmPassword = document.getElementById("confirmPassword");

    form.addEventListener("submit", function(event) {
        if (password.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity("Las contraseñas no coinciden");
            event.preventDefault();
            event.stopPropagation();
        } else {
            confirmPassword.setCustomValidity("");
        }

        form.classList.add("was-validated");
    }, false);
});