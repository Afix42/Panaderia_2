from django.contrib import admin
from .models import Rol,Usuario,Comuna,Direccion,Venta,Producto,Comentario,Detalle

# Register your models here.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Comentario)
admin.site.register(Detalle)
