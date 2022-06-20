from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto, Usuario, Rol
from .serializers import ProductoSerializers, UsuarioSerializers, RolSerializers
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def EliminarModificarProducto(request, id):
    try:
        p = Producto.objects.get(idProducto = id)
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializers(p)
        return Response(serializer.data)


    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializers(p, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        p.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarProducto(request):
    data = JSONParser().parse(request)
    serializer = ProductoSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listarProductos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializers(productos,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializers(usuarios,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listarRol(request):
    roles = Rol.objects.all()
    serializer = RolSerializers(roles,many=True)
    return Response(serializer.data)
        
