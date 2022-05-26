from django.contrib import admin
from django.urls import path
from .views import inicio,registro,login,registro_usuario,agregar_producto

urlpatterns = [
    path('', inicio, name='menu'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('registro_usuario', registro_usuario, name='registro_usuario'),
    path('agregar_producto', agregar_producto, name='agregar_producto'),

]