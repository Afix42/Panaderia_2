from django.contrib import admin
from django.urls import path
from .views import inicio,registro,login,registro_usuario,agregar_producto,vista_usuario,login_usuario,vista_admin

urlpatterns = [
    path('', inicio, name='menu'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('registro_usuario', registro_usuario, name='registro_usuario'),
    path('agregar_producto', agregar_producto, name='agregar_producto'),
    path('login_usuario', login_usuario, name='login_usuario'),
    path('vista_usuario',vista_usuario, name='vista_usuario'),
    path('vista_admin',vista_admin,name='vista_admin'),
]