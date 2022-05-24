const nomProd = document.getElementById("nomProd");
const descProd = document.getElementById("descProd");
const precio = document.getElementById("precio");
const cantidad = document.getElementById("cantidad");
const form = document.getElementById("form");
const listInputs = document.querySelectorAll(".form-input");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  let condicion = validacionForm();
  if (condicion) {
    enviarFormulario();
  }
});

function validacionForm() {
  form.lastElementChild.innerHTML = "";
  let condicion = true;
  listInputs.forEach((element) => {
    element.lastElementChild.innerHTML = "";
  });

  if (nomProd.value.length < 4 || nomProd.value.trim() == "") {
    mostrarMensajeError("nomProd", "Nombre del producto muy corta, tiene que ser mayor a 4 letras*");
    condicion = false;
  }
  if (descProd.value.length < 20 || descProd.value.trim() == "") {
    mostrarMensajeError("descProd", "Descripcion  muy corta, tiene que tener 20 letras minimo*");
    condicion = false;
  }
  if (precio.value.length < 100 || precio.value.trim() == "") {
    mostrarMensajeError("precio", "Precio no valido, tiene que ser mayor a 100$*");
    condicion = false;
  }
  if (cantidad.value.length < 1 || cantidad.value.trim() == "") {
    mostrarMensajeError("cantidad", "Cantidad no valida*");
    condicion = false;
  }
 
}

function mostrarMensajeError(claseInput, mensaje) {
  let elemento = document.querySelector(`.${claseInput}`);
  elemento.lastElementChild.innerHTML = mensaje;
}

function enviarFormulario() {
  form.reset();
  form.lastElementChild.innerHTML = "Listo !!";
}


