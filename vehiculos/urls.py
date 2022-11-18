from .views import homeTemplateView, vehiculosTemplateView, entregasTemplateView, almacenTemplateView, vehiculosPageDetail, vehiculosPagesCreate, vehiculosPageUpdate, vehiculosPageDelete, ComentariosCreateView, ComentariosDeleteView
from django.urls import path

urlpatterns = [
    path('',homeTemplateView.as_view(), name='home'),
    path('vehiculos/',vehiculosTemplateView.as_view(), name='vehiculos'),
    path('entregas/',entregasTemplateView.as_view(), name='entregas'),
    path('almacen/',almacenTemplateView.as_view(), name='almacen'),
### Detalle
    path('vehiculos/<int:pk>/', vehiculosPageDetail.as_view(), name='vehiculos_detalle'),
### Crear
    path('vehiculos/nuevo/', vehiculosPagesCreate.as_view(), name="vehiculos_nuevo"),
### Modificar
    path('vehiculos/<int:pk>/editar/', vehiculosPageUpdate.as_view(), name="vehiculos_editar"),

### Borrar 
    path('vehiculos/<int:pk>/eliminar/', vehiculosPageDelete.as_view(), name="vehiculos_eliminar"),

### Comentario
    path('<int:pk>/Comentario/',ComentariosCreateView.as_view(), name='Comentario'),

    path('<int:pk>/Comentario_eliminar/',ComentariosDeleteView.as_view(), name='Comentario_eliminar'),


]