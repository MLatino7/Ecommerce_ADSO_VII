from django.urls import path, include
from django.urls import re_path
from rest_framework import routers
from api_drf import views
from .views import Producto



router = routers.DefaultRouter()
router.register('producto', views.ProductosViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('productos/', Producto, name='productos_list'),

]
