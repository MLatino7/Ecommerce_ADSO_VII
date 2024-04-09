import json
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Empleados, Producto, Categoria,SubcategoriaProducto
from datetime import date



@method_decorator(csrf_exempt, name='dispatch')
class VistaEmpleados(View):
    def get(self, request):
        empleados = list(Empleados.objects.values())
        if empleados:
            return JsonResponse({'message': "Success", 'empleados': empleados})
        else:
            return JsonResponse({'message': "Company not found..."})

    def post(self, request):
        # Implementa la lógica para crear un nuevo empleado
        pass

    def delete(self, request):
        # Implementa la lógica para eliminar un empleado existente
        pass

    def put(self, request):
        # Implementa la lógica para actualizar un empleado existente
        pass

@method_decorator(csrf_exempt, name='dispatch')
class VistaProductos(View):
    def get(self, request):
        productos = list(Producto.objects.values())
        if productos:
            return JsonResponse({'message': "Success", 'productos': productos})
        else:
            return JsonResponse({'message': "Company not found..."})

    def post(self, request):
        try:
            data = json.loads(request.body)
            # Obtén objetos Categoria y Subcategoria correspondientes
            categoria_id = data.get('categoria_id', None)
            subcategoria_id = data.get('subcategoria_id', None)
            categoria = Categoria.objects.get(id=categoria_id) if categoria_id else None
            subcategoria = SubcategoriaProducto.objects.get(id=subcategoria_id) if subcategoria_id else None
        
            producto = Producto.objects.create(
                nombre=data['nombre'],
                descripcion=data['descripcion'],
                valor=data['valor'],
                fecha_modificacion='2024-03-20',
                estado_producto=data['estado'],
                fecha_ingreso='2024-03-20',
                categoria_id='1',
                subcategoria_id='2',
            )

            return JsonResponse({'message': 'Producto creado con éxito', 'id': producto.id}, status=201)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

    def delete(self, request):
        # Implementa la lógica para eliminar un producto existente
        pass

    def put(self, request):
        # Implementa la lógica para actualizar un producto existente
        pass