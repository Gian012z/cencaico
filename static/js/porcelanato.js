function toggleButton1() {
    var nombre = document.getElementById("nombre").value.trim();
    var numero = document.getElementById("numero").value.trim();
    var boton = document.getElementById("first-btn")

    if (nombre && numero) {
        boton.style.display = "block";  // Muestra el botón
        boton.style.animation = "fadeIn 0.3s ease-in-out";  // Aplica la animación
    } else {
        boton.style.display = "none";  // Oculta el botón
    }
}

function toggleButton2() {
    var rubro = document.getElementById("rubro").value.trim();
    var boton = document.getElementById("third-btn")

    if (rubro) {
        boton.style.display = "block";  // Muestra el botón
        boton.style.animation = "fadeIn 0.3s ease-in-out";  // Aplica la animación
    } else {
        boton.style.display = "none";  // Oculta el botón
    }
}

function toggleButton3() {
    var disponibilidad = document.getElementById("disponibilidad").value.trim();
    var boton = document.getElementById("fourth-btn")

    if (disponibilidad) {
        boton.style.display = "block";  // Muestra el botón
        boton.style.animation = "fadeIn 0.3s ease-in-out";  // Aplica la animación
    } else {
        boton.style.display = "none";  // Oculta el botón
    }
}

function toggleButton4() {
    var inicio_curso = document.getElementById("inicio-curso").value.trim();
    var boton = document.getElementById("fifth-btn")

    if (inicio_curso) {
        boton.style.display = "block";  // Muestra el botón
        boton.style.animation = "fadeIn 0.3s ease-in-out";  // Aplica la animación
    } else {
        boton.style.display = "none";  // Oculta el botón
    }
}

function toggleButton5() {
    var costos = document.getElementById("costos").value.trim();
    var boton = document.getElementById("sixth-btn")

    if (costos) {
        boton.style.display = "block";  // Muestra el botón
        boton.style.animation = "fadeIn 0.3s ease-in-out";  // Aplica la animación
    } else {
        boton.style.display = "none";  // Oculta el botón
    }
}
