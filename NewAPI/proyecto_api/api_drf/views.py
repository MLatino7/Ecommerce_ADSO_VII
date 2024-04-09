from django.shortcuts import render
from rest_framework import viewsets
from api_drf.serializer import ProductosSerializer
from .models import Producto


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer