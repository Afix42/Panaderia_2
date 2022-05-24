from django.contrib import admin
from django.urls import path
from .views import inicio,registro,login

urlpatterns = [
    path('', inicio, name='menu'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
]