from rest_framework import serializers
from core.models import Producto, Usuario, Rol

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','descripcionProducto', 'total']


class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario', 'nombreUsuario', 'apellidoUsuario', 'correoUsuario']


class RolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['idRol', 'nombreRol']
