from django.urls import path
from api_rest.views import agregarProducto, EliminarModificarProducto, listarProductos, listarUsuarios, listarRol, EliminarModificarUsuario, agregarUsuario, EliminarModificarRol, agregarRol
from api_rest.viewsLogin import loginApi


urlpatterns = [
    path('agregarProducto', agregarProducto, name='agregarProducto'),
    path('EliminarModificarProducto/<id>',EliminarModificarProducto,name='EliminarModificarProducto'),
    path('listarProductos', listarProductos, name='listarProductos'),
    path('listarUsuarios', listarUsuarios, name='listarUsuarios'),
    path('listarRol', listarRol, name='listarRol'),
    path('loginApi',loginApi,name='loginApi'),
    path('EliminarModificarUsuario/<id>',EliminarModificarUsuario,name='EliminarModificarUsuario'),
    path('agregarUsuario',agregarUsuario,name='agregarUsuario'),
    path('EliminarModificarRol/<id>',EliminarModificarRol,name='EliminarModificarRol'),
    path('agregarRol',agregarRol,name='agregarRol'),
]