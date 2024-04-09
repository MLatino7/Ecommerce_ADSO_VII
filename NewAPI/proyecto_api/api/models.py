# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CarritoCompras(models.Model):
    id = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_productos = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_productos', blank=True, null=True)
    email_cliente = models.CharField(max_length=25, blank=True, null=True)
    fecha_cotizacion = models.DateField(blank=True, null=True)
    valor_total = models.IntegerField(blank=True, null=True)
    medio_pago = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrito_compras'


class Categoria(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'categoria'


class Empleados(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    edad = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'


class FacturaProductosUsuarios(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, factura_id, producto_id, usuario_id) found, that is not supported. The first column is selected.
    factura = models.ForeignKey('Facturas', models.DO_NOTHING)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)
    unidades = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_productos_usuarios'
        unique_together = (('id', 'factura', 'producto', 'usuario'),)


class Facturas(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, usuario_id) found, that is not supported. The first column is selected.
    numero_factura = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    nombre_cliente = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    fecha_facturacion = models.DateField(blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    valor_total = models.IntegerField(blank=True, null=True)
    estado_factura = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'facturas'
        unique_together = (('id', 'usuario'),)


class Imagenes(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    ruta = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes'


class Inventario(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, carrito_compras_id) found, that is not supported. The first column is selected.
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad_disponible = models.IntegerField(blank=True, null=True)
    cantidad_ventas = models.IntegerField(blank=True, null=True)
    carrito_compras_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario'
        unique_together = (('id', 'carrito_compras_id'),)


class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    valor = models.IntegerField(blank=True, null=True)
    fecha_modificacion = models.CharField(max_length=100, blank=True, null=True)
    estado_producto = models.CharField(max_length=100, blank=True, null=True)
    fecha_ingreso = models.CharField(max_length=100, blank=True, null=True)
    categoria_id = models.IntegerField(max_length=100, blank=True, null=True)
    subcategoria_id = models.IntegerField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class SubcategoriaProducto(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    categoria_id = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategoria_producto'


class Usuarios(models.Model):
    id_usuario = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)
    telefono = models.IntegerField()
    permisos = models.CharField(max_length=50)
    estado_usuario = models.IntegerField()
    rol = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
