from django.shortcuts import render, redirect
from .models import Producto, Usuario, Rol
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'core/Menu.html')

def registro(request):
    return render(request,'core/formularioRegistro.html')

def login(request):
    return render(request, 'core/FormularioLogin.html')

def formulario_producto(request):
    return render(request, 'core/FormularioAgregarProductos.html')

def vista_usuario(request):
    return render(request,'core/menuUsuario.html')

def vista_admin(request):
    return render(request, 'core/MenuAdmin.html')

def berlin(request):
    return render(request,'core/plantillaProducto.html')
    
def lista_producto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/ListaProductos.html', data)

def registro_usuario(request):
    nombre_u = request.POST['nombre']
    apellido_u = request.POST['apellido']
    correo_u = request.POST['email']
    celular_u = request.POST['celular']
    clave_u = request.POST['password']

    #insert
    roluser = Rol.objects.get(nombreRol= "Usuario")
    Usuario.objects.create(nombreUsuario = nombre_u, apellidoUsuario = apellido_u, correoUsuario = correo_u, celularUsuario = celular_u, clave = clave_u, rol = roluser)
    
    messages.success(request,'Usuario Registrado')

    return redirect('login')

def form_producto(request):
    nombre_p = request.POST['nomProd']
    desc_p = request.POST['descProd']
    total_p = request.POST['precio']
    stock_p = request.POST['cantidad']
    img_foto = request.FILES['foto_m']


    #insert
    Producto.objects.create(nombreProducto = nombre_p,descripcionProducto = desc_p, total = total_p, stock =stock_p,foto = img_foto)

    messages.success(request,'Producto agregado')

    return redirect('formulario_producto')

def login_usuario(request):
    nombre = request.POST['nombre']
    password = request.POST['password']
    
    try:
        us = Usuario.objects.get(nombreUsuario= nombre, clave = password)
        rol2 = Rol.objects.get(nombreRol= "Administrador")
        if us.rol ==  rol2:                  
            return redirect('vista_admin')
        else:
            return redirect('vista_usuario')
    except Usuario.DoesNotExist:
        messages.error(request,'Usuario y/o Contraseña Incorrecta')
        return redirect('login')
    