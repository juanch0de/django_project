from django.urls import path
from .views import hello_world
from .views import lista_productos

from . import views

urlpatterns = [
        path("productos/", lista_productos),
        path("<str:name>/", hello_world),
]
