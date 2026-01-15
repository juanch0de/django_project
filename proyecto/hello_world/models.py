from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique = True, null = False, blank = False)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
