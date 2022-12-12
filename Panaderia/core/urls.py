from django.contrib import admin
from django.urls import path
from .views import inicio,registro,login,registro_usuario,form_producto,vista_usuario,login_usuario,vista_admin,berlin,formulario_producto,lista_producto,lista_productos_admin,lista_productos_usuario, edicion_prod, editar_producto, eliminacion_prod,carrito,carrito2, elimCarrito

urlpatterns = [
    path('', inicio, name='menu2'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('registro_usuario', registro_usuario, name='registro_usuario'),
    path('form_producto', form_producto, name='form_producto'),
    path('formulario_producto',formulario_producto, name='formulario_producto'),
    path('login_usuario', login_usuario, name='login_usuario'),
    path('vista_usuario',vista_usuario, name='vista_usuario'),
    path('vista_admin',vista_admin,name='vista_admin'),
    path('berlin',berlin,name='berlin'),
    path('lista_producto',lista_producto,name='lista_producto'),
    path('lista_productos_admin',lista_productos_admin,name='lista_productos_admin'),
    path('lista_productos_usuario',lista_productos_usuario,name='lista_productos_usuario'),
    path('edicion_prod/<idProducto>', edicion_prod, name='edicion_prod'),
    path('editar_producto', editar_producto, name='editar_producto'),
    path('eliminacion_prod/<idProducto>', eliminacion_prod, name='eliminacion_prod'),
    path('carrito',carrito,name='carrito'),
    path('carrito2',carrito2,name='carrito2'),
    path('elimCarrito/<idDetalle>',elimCarrito,name='elimCarrito'),
]