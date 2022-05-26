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
    correo_u = request.POST['correo']
    celular_u = request.POST['celular']

    #insert
    Usuario.objects.create(nombreUsuario = nombre_u, apellidoUsuario = apellido_u, correoUsuario = correo_u, celularUsuario = celular_u)
    
    messages.success(request,'Usuario Registrado')

    return redirect('login')

def agregar_producto(request):
    nombre_p = request.POST['nombre']
    desc_p = request.POST['descripcion']
    img_foto = request.FILES['foto_m']
    total_p = request.POST['precio']
    stock_p = request.POST['stock']

    #insert
    Producto.objects.create(nombreProducto = nombre_p,descripcionProducto = desc_p, foto = img_foto, total = total_p, stock =stock_p)

    messages.success(request,'Producto agregado')

    return redirect('form_producto')

def login_usuario(request):
    nombre = request.POST['nombre']
    password = request.POST['password']

    try:
        usuario = Usuario.objects.get(nombreUsuario = nombre,clave = password)
        # aqui llamo a la vista del html si los datos son correctos utilizando return redirect('vista usuario')
    except:
        messages.error(request,'Usuario y/o contraseña incorrectos')
        return redirect('login')









