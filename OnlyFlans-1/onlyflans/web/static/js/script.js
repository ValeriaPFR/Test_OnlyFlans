document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("registroClienteForm").addEventListener("submit", function (event) {
        event.preventDefault();

        // Obtener los datos del formulario
        const nombre = document.getElementById("firstName").value;
        const apellido = document.getElementById("lastName").value;
        const email = document.getElementById("email").value;
        const edad = document.getElementById("age").value;

        // Realizar la petición POST al backend de Django
        fetch("{% url 'new_client' %}", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify({
                nombre: nombre,
                apellido: apellido,
                email: email,
                edad: edad
                // Agrega los demás campos del formulario aquí
            })
        })
            .then(response => {
                if (response.ok) {
                    window.location.href = "{% url 'new_client' %}";
                } else {
                    alert("Hubo un error al procesar tu solicitud. Por favor, intenta nuevamente.");
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Hubo un error al procesar tu solicitud. Por favor, intenta nuevamente.");
            });
    });
});


