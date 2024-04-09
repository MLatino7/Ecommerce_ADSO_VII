from django.urls import path
from django.urls import re_path
from .views import Empleados
from .views import VistaEmpleados
from .views import VistaProductos







urlpatterns = [
    path('empleados/', VistaEmpleados.as_view(), name='empleados_list'),
    path('productos/', VistaProductos.as_view(), name='productos_list'),

]
