from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Producto

def hello_world(request, name):
    return HttpResponse(f"Hello World! Qhubo {name}!!!")

def lista_productos(request):
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

    return JsonResponse(data, safe=False)

def producto_individual(request, identificador):
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
            "nombre": producto.codigo,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
            "cantidad": producto.cantidad, 
    }

    return JsonResponse(data)
