
from django.http        import Http404
from django.shortcuts   import redirect, render

from django.views.generic import TemplateView

from .forms    import CrearProductoForm, ActualizarProductoForm
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
        except Exception :
            raise Http404('Error al consumir el microservicio de productos')
        
        return redirect('productos_app:consultar-productos-page')


def inhabilitar_producto(id):
    try:
        inhabilitar_producto_ms(id)
    except Exception :
        raise Http404('Error al consumir el microservicio de productos')
    
    return redirect('productos_app:consultar-productos-page')


def actualiza_producto(request, id):
    if request.method == 'GET':
        form = ActualizarProductoForm()
    else:
        form = ActualizarProductoForm(request.POST)
        if form.is_valid():
            nombre   = request.POST.get('nombre')
            precio   = float(request.POST.get('precio'))
            cantidad = int(request.POST.get('cantidad'))

            json_parametro = {'nombre':nombre, 'precio':precio, 'cantidad':cantidad}

            try:
                actualizar_producto_ms(json_parametro,id)
            except Exception :
                raise Http404('Error al consumir el microservicio de productos')
            return redirect('productos_app:consultar-productos-page')

    return render(request, 'productos/actualizar_producto.html',{'form':form})