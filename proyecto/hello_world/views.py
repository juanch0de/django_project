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
