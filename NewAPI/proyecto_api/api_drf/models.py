from django.db import models

from rest_framework.views import APIView

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    valor = models.CharField(max_length=100, blank=True, null=True)
    fecha_modificacion = models.CharField(max_length=100, blank=True, null=True)
    estado_producto = models.CharField(max_length=100, blank=True, null=True)
    fecha_ingreso = models.CharField(max_length=100, blank=True, null=True)
    categoria_id = models.CharField(max_length=100, blank=True, null=True)
    subcategoria_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

        