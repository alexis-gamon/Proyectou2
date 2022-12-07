

from .views import homeTemplateView, vehiculosTemplateView, entregasTemplateView, almacenTemplateView, vehiculosPageDetail, vehiculosPagesCreate, vehiculosPageUpdate, vehiculosPageDelete, ComentariosCreateView, ComentariosDeleteView, entregasPageDetail, entregasPagesCreate, entregasPageUpdate, entregasPageDelete, almacenPageDetail, almacenPagesCreate, almacenPageUpdate, almacenPageDelete, ubicacionTemplateView, ubicacionPageDetail, ubicacionPagesCreate, ubicacionPageUpdate, ubicacionPageDelete
from django.urls import path

urlpatterns = [
    path('',homeTemplateView.as_view(), name='home'),
    path('vehiculos/',vehiculosTemplateView.as_view(), name='vehiculos'),
    path('entregas/',entregasTemplateView.as_view(), name='entregas'),
    path('/almacen/',almacenTemplateView.as_view(), name='almacen'),
    path('/ubicacion/',ubicacionTemplateView.as_view(), name='ubicacion'),
    

    ####################        VEHICULOS    #############################################

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

    path('vehiculos/<int:pk>/Comentario_eliminar/',ComentariosDeleteView.as_view(), name='Comentario_eliminar'),


####################        ENTREGAS    #############################################


### Detalle
    path('entregas/<int:pk>/', entregasPageDetail.as_view(), name='entregas_detalle'),
### Crear
    path('entregas/nuevo/', entregasPagesCreate.as_view(), name="entregas_nuevo"),
### Modificar
    path('entregas/<int:pk>/editar/', entregasPageUpdate.as_view(), name="entregas_editar"),

### Borrar 
    path('entregas/<int:pk>/eliminar/', entregasPageDelete.as_view(), name="entregas_eliminar"),

### Comentario
    path('<int:pk>/Comentario/',ComentariosCreateView.as_view(), name='Comentario'),

 ##   path('<int:pk>/Comentario_eliminar/',ComentariosDeleteView.as_view(), name='Comentario_eliminar'),

####################        ALMACEN    #############################################

### Detalle
    path('almacen/<int:pk>/', almacenPageDetail.as_view(), name='almacen_detalle'),
### Crear
    path('almacen/nuevo/', almacenPagesCreate.as_view(), name="almacen_nuevo"),
### Modificar
    path('almacen/<int:pk>/editar/', almacenPageUpdate.as_view(), name="almacen_editar"),

### Borrar 
    path('almacen/<int:pk>/eliminar/', almacenPageDelete.as_view(), name="almacen_eliminar"),

### Comentario
    path('<int:pk>/Comentario/',ComentariosCreateView.as_view(), name='Comentario'),

  ##  path('<int:pk>/Comentario_eliminar/',ComentariosDeleteView.as_view(), name='Comentario_eliminar'),

####################        UBICACION    #############################################

### Detalle
    path('ubicacion/<int:pk>/', ubicacionPageDetail.as_view(), name='ubicacion_detalle'),
### Crear
    path('ubicacion/nuevo/', ubicacionPagesCreate.as_view(), name="ubicacion_nuevo"),
### Modificar
    path('ubicacion/<int:pk>/editar/', ubicacionPageUpdate.as_view(), name="ubicacion_editar"),

### Borrar 
    path('ubicacion/<int:pk>/eliminar/', ubicacionPageDelete.as_view(), name="ubicacion_eliminar"),


]