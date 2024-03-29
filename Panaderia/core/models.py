from pickle import FALSE
from django.db import models

# Create your models here.

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True, verbose_name='id del rol')
    nombreRol = models.CharField(max_length=20, verbose_name='Nombre del rol', blank=True, null=True)

    def __str__(self):
        return self.nombreRol

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='id de usuario')
    nombreUsuario = models.CharField(max_length=25, verbose_name='Nombre del usuario', blank=False, null=False)
    clave = models.CharField(max_length=30,verbose_name='Contraseña',blank=True,null=True)
    apellidoUsuario = models.CharField(max_length=25, verbose_name='Apellido del usuario', blank=False, null=False)
    correoUsuario = models.CharField(max_length=25, verbose_name='Correo del usuario', blank=False, null=False)
    celularUsuario = models.IntegerField(verbose_name='Celular del usuario')
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombreUsuario

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True, verbose_name='id de la comuna')
    descripcionComuna = models.CharField(max_length=100, verbose_name='Descripcion de la comuna', blank=False, null=False)

    def __str__(self):
        return self.descripcionComuna

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True, verbose_name='id de la direccion')
    descripcionDireccion = models.CharField(max_length=100, verbose_name='Descripcion de la direccion', blank=False, null=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionDireccion  

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True, verbose_name='id de la venta')
    fVenta = models.DateField(auto_now=True ,verbose_name='fecha venta')
    total = models.IntegerField(verbose_name='Total de la venta')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name='Estatus de la venta', null=True, blank=True)

    def __str__(self):
        return str(self.idVenta)

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='id del producto')
    nombreProducto = models.CharField(max_length=25, verbose_name='Nombre del producto', blank=False, null=False)
    descripcionProducto = models.CharField(max_length=300, verbose_name='Descripcion del producto', blank=False, null=False)
    foto = models.ImageField(upload_to="producto", null= True)
    total = models.IntegerField(verbose_name='Precio del producto')
    stock = models.IntegerField(verbose_name='Stock del producto')

    def __str__(self):
        return self.nombreProducto

class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True, verbose_name='id del comentario')
    descripcionComentario = models.CharField(max_length=100, verbose_name='Descripcion del comentario', blank=False, null=False)
    baneo = models.IntegerField(verbose_name='Estado del baneo')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionComentario

class Detalle(models.Model):
    idDetalle = models.AutoField(primary_key=True, verbose_name='id del detalle compra')
    cantidad = models.IntegerField(verbose_name='Cantidad de la compra')
    subtotal = models.IntegerField(verbose_name='Subtotal de la compra')
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.subtotal)