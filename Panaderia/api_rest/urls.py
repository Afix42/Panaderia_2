from django.urls import path
from api_rest.views import agregarProducto, EliminarModificarProducto, listarProductos, listarUsuarios, listarRol
from api_rest.viewsLogin import loginApi


urlpatterns = [
    path('agregarProducto', agregarProducto, name='agregarProducto'),
    path('EliminarModificarProducto/<id>',EliminarModificarProducto,name='EliminarModificarProducto'),
    path('listarProductos', listarProductos, name='listarProductos'),
    path('listarUsuarios', listarUsuarios, name='listarUsuarios'),
    path('listarRol', listarRol, name='listarRol'),
    path('loginApi',loginApi,name='loginApi'),
]