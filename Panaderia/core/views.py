from django.shortcuts import render, redirect
from .models import Producto, Usuario
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'core/Menu.html')

def registro(request):
    return render(request,'core/formularioRegistro.html')

def login(request):
    return render(request, 'core/FormularioLogin.html')

def form_producto(request):
    return render(request, 'core/FormularioAgregarProductos.html')

def registro_usuario(request):
    nombre_u = request.POST['nombre']
    apellido_u = request.POST['apellido']
    correo_u = request.POST['email']
    celular_u = request.POST['celular']
    clave_u = request.POST['password']

    #insert
    Usuario.objects.create(nombreUsuario = nombre_u, apellidoUsuario = apellido_u, correoUsuario = correo_u, celularUsuario = celular_u, clave = clave_u)
    
    messages.success(request,'Usuario Registrado')

    return redirect('login')

def agregar_producto(request):
    nombre_p = request.POST['nomProd']
    desc_p = request.POST['descProd']
    img_foto = request.FILES['foto_m']
    total_p = request.POST['precio']
    stock_p = request.POST['cantidad']

    #insert
    Producto.objects.create(nombreProducto = nombre_p,descripcionProducto = desc_p, foto = img_foto, total = total_p, stock =stock_p)

    messages.success(request,'Producto agregado')

    return redirect('form_producto')

def login_usuario(request):
    nombre = request.POST['nombre']
    password = request.POST['password']

    try:
        usuario = Usuario.objects.get(nombreUsuario = nombre,clave = password)
        if usuario.rol.idRol == 1:
            return
        # aqui llamo a la vista del html si los datos son correctos utilizando return redirect('vista administradr')   
        elif usuario.rol.idRol == 2:
            return
        # aqui llamo a la vista del html si los datos son correctos utilizando return redirect('vista usuario')
    except:
        messages.error(request,'Usuario y/o contraseña incorrectos')
        return redirect('login')