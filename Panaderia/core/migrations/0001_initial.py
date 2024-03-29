# Generated by Django 4.0.4 on 2022-05-31 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False, verbose_name='id de la comuna')),
                ('descripcionComuna', models.CharField(max_length=100, verbose_name='Descripcion de la comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('idDireccion', models.AutoField(primary_key=True, serialize=False, verbose_name='id de la direccion')),
                ('descripcionDireccion', models.CharField(max_length=100, verbose_name='Descripcion de la direccion')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='id del producto')),
                ('nombreProducto', models.CharField(max_length=25, verbose_name='Nombre del producto')),
                ('descripcionProducto', models.CharField(max_length=100, verbose_name='Descripcion del producto')),
                ('foto', models.ImageField(null=True, upload_to='producto')),
                ('total', models.IntegerField(verbose_name='Precio del producto')),
                ('stock', models.IntegerField(verbose_name='Stock del producto')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False, verbose_name='id del rol')),
                ('nombreRol', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombre del rol')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='id de usuario')),
                ('nombreUsuario', models.CharField(max_length=25, verbose_name='Nombre del usuario')),
                ('clave', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contraseña')),
                ('apellidoUsuario', models.CharField(max_length=25, verbose_name='Apellido del usuario')),
                ('correoUsuario', models.CharField(max_length=25, verbose_name='Correo del usuario')),
                ('celularUsuario', models.IntegerField(verbose_name='Celular del usuario')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='id de la venta')),
                ('fVenta', models.IntegerField(verbose_name='f venta')),
                ('total', models.IntegerField(verbose_name='Total de la venta')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.direccion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('idDetalle', models.AutoField(primary_key=True, serialize=False, verbose_name='id del detalle compra')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de la compra')),
                ('subtotal', models.IntegerField(verbose_name='Subtotal de la compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idComentario', models.AutoField(primary_key=True, serialize=False, verbose_name='id del comentario')),
                ('descripcionComentario', models.CharField(max_length=100, verbose_name='Descripcion del comentario')),
                ('baneo', models.IntegerField(verbose_name='Estado del baneo')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
