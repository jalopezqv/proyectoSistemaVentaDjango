from django.http import Http404
from django.shortcuts import render

from django.views.generic import TemplateView

from .services import consultar_productos_ms

# Create your views here.

def consultar_productos(request):
    try:
        productos = consultar_productos_ms()
    except Exception :
        raise Http404("Error al consumir el microservicio de productos")
    
    return render(request, 'productos/consultar-productos.html',{'productos':productos})



class CrearProducto(TemplateView):
    template_name = "productos/crear_producto.html"
    
