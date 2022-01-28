from django.urls    import path

from . import views

app_name = 'productos_app'

urlpatterns = [
    path('consultar-productos',       views.consultar_productos,     name='consultar-productos-page' ),
    path('crear-producto',            views.CrearProducto.as_view(), name='crear-producto-page'      ),
    path('inhabilitar-producto/<id>', views.inhabilitar_producto,    name='inhabilitar-producto-page'),
    path('actualiza-producto/<id>',   views.actualiza_producto,      name='actualiza-producto-page'  ),
]
