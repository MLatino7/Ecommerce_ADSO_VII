# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'categoria'


class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_modificacion = models.DateField()
    estado_producto = models.IntegerField()
    fecha_ingreso = models.DateField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    subcategoria = models.ForeignKey('SubcategoriaProducto', models.DO_NOTHING, blank=True, null=True)

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
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
