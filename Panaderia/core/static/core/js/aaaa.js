const nomProd = document.getElementById("nomProd");
const descProd = document.getElementById("descProd");
const precio = document.getElementById("precio");
const cantidad = document.getElementById("cantidad");
const form = document.getElementById("form");
const listInputs = document.querySelectorAll(".form-input");
const msj = document.getElementById("mensajeError")


form.addEventListener("submit",e =>{
    let msjMostrar = "";
    let envioCorrecto = false;

    if (nomProd.value.length < 4 || nomProd.value.length > 30) {
        msjMostrar += "Nombre del producto muy corta, tiene que ser mayor a 4 letras*<br>";
        envioCorrecto = true;
    }
    
    if(descProd.value.length <10 || descProd.value.length > 70){
        msjMostrar += "Descripcion  muy corta, tiene que tener 10 letras minimo*<br>";
        envioCorrecto = true;
    }

    if(precio.value.length <100 || precio.value.length > 50000){
        msjMostrar += "Precio no valido, tiene que ser mayor a 100$*<br>";
        envioCorrecto = true;
    }

    if(correo.value.length <1 || correo.value.length > 1000){
        msjMostrar += "Cantidad no valida,Tiene que ser mayor a 1*<br>";
        envioCorrecto = true;
    }

    if(envioCorrecto){
        msj.innerHTML = msjMostrar;
    }
    else{
        msj.innerHTML = "Formulario Enviado";
    }
    return condicion;
});