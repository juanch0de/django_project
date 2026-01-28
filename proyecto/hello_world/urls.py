from django.urls import path
from .views import hello_world
from .views import productos

from . import views

urlpatterns = [
        path("productos/<str:identificador>", views.producto_individual),
        path("productos/", productos),
]
