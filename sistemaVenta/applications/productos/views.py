
from django.http        import Http404
from django.shortcuts   import redirect, render

from django.views.generic import TemplateView

from .forms    import CrearProductoForm
from .services import *

# Create your views here.

def consultar_productos(request):
    try:
        productos = consultar_productos_ms()
    except Exception :
        raise Http404('Error al consumir el microservicio de productos')
    
    return render(request, 'productos/consultar-productos.html',{'productos':productos})
    
class CrearProducto(TemplateView):
    template_name = 'productos/crear_producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CrearProductoForm()

        return context

    def post(self, request):
        nombre   = request.POST.get('nombre')
        precio   = float(request.POST.get('precio'))
        cantidad = int(request.POST.get('cantidad'))

        json_parametro = {'nombre':nombre, 'precio':precio, 'cantidad':cantidad}

        try:
            crear_producto_ms(json_parametro)
            productos = consultar_productos_ms()
        except Exception :
            raise Http404('Error al consumir el microservicio de productos')
        
        return redirect('productos_app:consultar-productos-page')


def inhabilitar_producto(request, id):
    try:
        inhabilitar_producto_ms(id)
    except Exception :
        raise Http404('Error al consumir el microservicio de productos')
    
    return redirect('productos_app:consultar-productos-page')