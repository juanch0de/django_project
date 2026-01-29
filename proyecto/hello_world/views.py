from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Producto
import json

def hello_world(request, name):
    return HttpResponse(f"Hello World! Qhubo {name}!!!")

@csrf_exempt
def productos(request):
    if request.method == "GET":
        productos = Producto.objects.all()

        data = [
            {
                "id": p.id,
                "codigo": p.codigo,
                "nombre": p.nombre,
                "descripcion": p.descripcion,
                "precio": p.precio,
                "cantidad": p.cantidad,
            }
            for p in productos
        ]
        return JsonResponse(data, safe = False)

    elif request.method == "POST":
        body = json.loads(request.body)

        producto = Producto.objects.create(
                codigo = body["codigo"],
                nombre = body["nombre"],
                descripcion = body["descripcion"],
                precio = body["precio"],
                cantidad = body["cantidad"],
                )
        return JsonResponse(
                {"id": producto.id},
                status = 201
                )
        
@csrf_exempt
def producto_individual(request, identificador):
    if request.method == "GET":
        try:
            if identificador.isdigit():
                producto = Producto.objects.get(id=int(identificador))

            else:
                producto = Producto.objects.get(codigo=identificador)

        except Producto.DoesNotExist:
            raise Http404("Producto no encontrado")

        data = {
                "id": producto.id,
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precio": producto.precio,
                "cantidad": producto.cantidad,
                }

        return JsonResponse(data)
    
    elif request.method == "DELETE":
        try:
            if identificador.isdigit():
                producto = Producto.objects.get(id=int(identificador))

            else:
                producto = Producto.objects.get(codigo=identificador)

        except Producto.DoesNotExist:
            raise Http404("Producto no encontrado")

        producto.delete()
        return JsonResponse(
                {},
                status = 204
                )
    elif request.method == "PUT":
        try:
            if identificador.isdigit():
                producto = Producto.objects.get(id=int(identificador))

            else:
                producto = Producto.objects.get(codigo=identificador)

        except Producto.DoesNotExist:
            raise Http404("Producto no encontrado")

        body = json.loads(request.body)

        if "codigo" in body:
            producto.codigo = body["codigo"]
        if "nombre" in body:
            producto.nombre = body["nombre"]
        if "descripcion" in body:
            producto.descripcion = body["descripcion"]
        if "precio" in body:
            producto.precio = body["precio"]
        if "cantidad" in body:
            producto.cantidad = body["cantidad"]

        producto.save()

        return JsonResponse({
            "id": producto.id,
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
            "cantidad": producto.cantidad,
            })


