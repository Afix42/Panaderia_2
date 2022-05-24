const nombre = document.getElementById("nombre");
const apellidos = document.getElementById("apellido");
const correo = document.getElementById("email");
const celular = document.getElementById("celular");
const contrasenia = document.getElementById("password");
const contrasenia2 = document.getElementById("repeatPassword");
const terminosYcondiciones = document.getElementById("terminos");
const form = document.getElementById("form");
const listInputs = document.querySelectorAll(".form-input");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  let condicion = validacionForm();
  if (condicion) {
    enviarFormulario();
  }

function validacionForm() {
  form.lastElementChild.innerHTML = "";
  let condicion = true;
  listInputs.forEach((element) => {
    element.lastElementChild.innerHTML = "";
  });

  if (nombre.value.length < 1 || nombre.value.trim() == "") {
    mostrarMensajeError("nombre", "Nombre no valido*");
    condicion = false;
  }
  if (apellidos.value.length < 1 || apellidos.value.trim() == "") {
    mostrarMensajeError("apellido", "Apellido no valido");
    condicion = false;
  }
  if (correo.value.length < 1 || correo.value.trim() == "") {
    mostrarMensajeError("email", "Correo no valido*");
    condicion = false;
  }
  if (
    celular.value.length != 9 ||
    celular.value.trim() == "" ||
    isNaN(celular.value)
  ) {
    mostrarMensajeError("celular", "Celular no valido*");
    condicion = false;
  }
  if (contrasenia.value.length < 6 || contrasenia.value.trim() == "") {
    mostrarMensajeError("password", "Contraseña muy corta, minimo 6 caracteres*");
    condicion = false;
  }

  var letraNombre = contrasenia.value.charAt(0);
  if (!esMayus(letraNombre)){
    mostrarMensajeError ("password","La primera letra tiene que ser mayuscula");
      envioCorrecto = false;
  }
  
  if (contrasenia2.value != contrasenia.value) {
    mostrarMensajeError("repeatPassword", "Las contraseñas son diferentes*");
    condicion = false;
  }
  if (!terminosYcondiciones.checked) {
    mostrarMensajeError("terminos", "Acepte las condiciones*");
    condicion = false;
  } else {
    mostrarMensajeError("terminos", "");
  }
  return condicion;
}
});

function mostrarMensajeError(claseInput, mensaje) {
  let elemento = document.querySelector(`.${claseInput}`);
  elemento.lastElementChild.innerHTML = mensaje;
}

function enviarFormulario() {
  form.reset();
  form.lastElementChild.innerHTML = "Listo !!";
}

function esMayus (letra){
  return letra == letra.toUpperCase();
};







