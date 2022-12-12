from django.shortcuts import render, redirect
from .models import Producto, Usuario, Rol, Detalle
from django.contrib import messages
from django_user_agents.utils import get_user_agent
# Create your views here.
def inicio(request):
    return render(request,'core/menu2.html')

def registro(request):
    return render(request,'core/formularioRegistro.html')

def login(request):
    return render(request, 'core/FormularioLogin.html')

def formulario_producto(request):
    return render(request, 'core/FormularioAgregarProductos.html')

def carrito(request):
    detalles = Detalle.objects.all()
    productos = Producto.objects.all()
    data = {
        'productos': productos,
        'detalles': detalles
    }
        
    return render(request, 'core/carrito.html', data)
def carrito2(request):
    return render(request, 'core/carrito.html')

def edicion_prod(request, idProducto):
    producto = Producto.objects.get(idProducto = idProducto)
    return render(request, 'core/formularioEditarProd.html', {"producto": producto})

def editar_producto(request):
    idProducto = request.POST['idProd']
    nombre_p = request.POST['nomProd']
    desc_p = request.POST['descProd']
    total_p = request.POST['precio']
    stock_p = request.POST['cantidad']


    producto=Producto.objects.get(idProducto=idProducto)
    if(request.FILES.get('foto_m')):
        img_foto = request.FILES['foto_m']
        producto.foto = img_foto
    


    producto.nombreProducto = nombre_p
    producto.descripcionProducto = desc_p
    producto.total = total_p
    producto.stock = stock_p
     
    print("hola2")
    producto.save()
    print("hola")
    messages.success(request, 'Producto modificado con éxito')

    return redirect('lista_productos_admin')

def eliminacion_prod(request, idProducto):
    producto = Producto.objects.get(idProducto = idProducto)
    producto.delete()
    messages.success(request, 'Producto eliminado con éxito')

    return redirect('lista_productos_admin')


def vista_usuario(request):
    return render(request,'core/menuUsuario.html')

def vista_admin(request):
    return render(request, 'core/MenuAdmin.html')

def berlin(request):
    return render(request,'core/plantillaProducto.html')

def lista_productos_admin(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'core/ListaProductosAdmin.html',data)

def lista_productos_usuario(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'core/ListaProductosUsuario.html',data)
    
def lista_producto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/ListaProductosTABLA.html', data)

def registro_usuario(request):
    nombre_u = request.POST['nombre']
    apellido_u = request.POST['apellido']
    correo_u = request.POST['email']
    celular_u = request.POST['celular']
    clave_u = request.POST['password']

    #insert
    roluser = Rol.objects.get(nombreRol= "Usuario")

    try:
        x = Usuario.objects.get(nombreUsuario = nombre_u)
        messages.error(request,'Error: Usuario ya existe')
        return redirect('registro')

    except Usuario.DoesNotExist:
        Usuario.objects.create(nombreUsuario = nombre_u, apellidoUsuario = apellido_u, correoUsuario = correo_u, celularUsuario = celular_u, clave = clave_u, rol = roluser)
    
        messages.success(request,'Usuario registrado con éxito')

        return redirect('login')


    
def form_producto(request):
    nombre_p = request.POST['nomProd']
    desc_p = request.POST['descProd']
    total_p = request.POST['precio']
    stock_p = request.POST['cantidad']
    #Para que el formulario se mande aun que la foto no este
    if request.FILES.get('foto_m'):
        img_foto = request.FILES['foto_m']
        Producto.objects.create(nombreProducto = nombre_p,descripcionProducto = desc_p, total = total_p, stock =stock_p,foto = img_foto)
    
    else:
        Producto.objects.create(nombreProducto = nombre_p,descripcionProducto = desc_p, total = total_p, stock =stock_p)

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
    

def elimCarrito(request, idDetalle):
    producto = Detalle.objects.get(idDetalle = idDetalle)
    producto.delete()
    messages.success(request, 'Producto eliminado con éxito')

    return redirect('carrito')

def my_view(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return HttpResponse('User using mobile')
    elif user_agent.is_pc:
        vi=request.META['HTTP_USER_AGENT']
        print(vi)
        return HttpResponse('User using Computer')