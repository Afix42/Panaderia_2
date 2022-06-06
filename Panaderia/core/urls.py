from django.contrib import admin
from django.urls import path
from .views import inicio,registro,login,registro_usuario,form_producto,vista_usuario,login_usuario,vista_admin,berlin,formulario_producto

urlpatterns = [
    path('', inicio, name='menu'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('registro_usuario', registro_usuario, name='registro_usuario'),
    path('form_producto', form_producto, name='form_producto'),
    path('formulario_producto',formulario_producto, name='formulario_producto'),
    path('login_usuario', login_usuario, name='login_usuario'),
    path('vista_usuario',vista_usuario, name='vista_usuario'),
    path('vista_admin',vista_admin,name='vista_admin'),
    path('berlin',berlin,name='berlin'),
]