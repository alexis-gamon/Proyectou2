
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import vehiculos, entregas, almacen, Comentario, ubicacion
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin##obliga a que estes logeado para poder visualizar una vista
from django.core.exceptions import PermissionDenied##valida los permisos


class homeTemplateView(TemplateView):
    template_name = 'home.html'
#########################################################################
class vehiculosTemplateView(LoginRequiredMixin, ListView):
    model = vehiculos
    template_name = 'vehiculos.html'
    context_object_name = 'Todos_Vehiculos'
    login_url = 'login'


class entregasTemplateView(LoginRequiredMixin, ListView):
    template_name = 'entregas.html'
    model = entregas
    context_object_name = 'Todas_Entregas'
    login_url = 'login'


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
        
    login_url = 'login'
class almacenTemplateView(LoginRequiredMixin, ListView):
    template_name = 'almacen.html'
    model = almacen
    context_object_name = 'Todos_almacen'
    login_url = 'login'


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
        
 
    login_url = 'login'

class ubicacionTemplateView(LoginRequiredMixin, ListView):
    model = ubicacion
    template_name = 'Ubicacion.html'
    context_object_name = 'Todos_Ubicacion'
    login_url = 'login'


#########################################################################

class vehiculosPageDetail(LoginRequiredMixin,DetailView):
    template_name = 'vehiculos_detalle.html'
    model = vehiculos
    context_object_name = 'Todos_Vehiculos'
    login_url = 'login'

class entregasPageDetail(LoginRequiredMixin,DetailView):
    template_name = 'entregas_detalle.html'
    model = entregas
    context_object_name = 'Todas_Entregas'
    login_url = 'login'

class almacenPageDetail(LoginRequiredMixin,DetailView):
    template_name = 'almacen_detalle.html'
    model = almacen
    context_object_name = 'Todos_almacen'
    login_url = 'login'

class ubicacionPageDetail(LoginRequiredMixin,DetailView):
    template_name = 'ubicacion_detalle.html'
    model = ubicacion
    context_object_name = 'Todos_Ubicacion'
    login_url = 'login'

#########################################################################
class vehiculosPagesCreate(LoginRequiredMixin,CreateView):
    template_name = 'vehiculos_nuevo.html'
    model = vehiculos
    fields = "__all__"
    login_url = 'login'


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
        
    login_url = 'login'
    

class entregasPagesCreate(LoginRequiredMixin,CreateView):
    template_name = 'entregas_nuevo.html'
    model = entregas
    fields = "__all__"
    login_url = 'login'


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
        
 
    login_url = 'login'

class almacenPagesCreate(LoginRequiredMixin,CreateView):
    template_name = 'almacen_nuevo.html'
    model = almacen
    fields = "__all__"
    login_url = 'login'


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
        
    #def dispatch(self, request, *args, **kwargs):
    #    obj = self.get_object()
    #    if request.user.is_superuser:
    ##        return super().dispatch(request, *args, **kwargs)
    #    raise PermissionDenied

class ubicacionPagesCreate(LoginRequiredMixin,CreateView):
    template_name = 'ubicacion_nuevo.html'
    model = ubicacion
    fields = "__all__"
    login_url = 'login'


    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
        
    login_url = 'login'



#########################################################################
class vehiculosPageUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'vehiculos_editar.html'
    model = vehiculos
    fields = ['Marca', 'Color']

   
    success_url = reverse_lazy('vehiculos')

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied


class entregasPageUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'entregas_editar.html'
    model = entregas
    fields = ['Serie', 'Cliente']
    
    success_url = reverse_lazy('entregas')

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

class almacenPageUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'almacen_editar.html'
    model = almacen
    fields = ['NumeroSerie', 'Lote']

   
    success_url = reverse_lazy('almacen')

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

class ubicacionPageUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'ubicacion_editar.html'
    model = ubicacion
    fields = ['Zona', 'CodigoPostal']

   
    success_url = reverse_lazy('ubicacion')

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied



#########################################################################
class vehiculosPageDelete(LoginRequiredMixin,DeleteView):
    template_name = 'vehiculos_eliminar.html'
    model = vehiculos
    success_url = reverse_lazy('vehiculos')

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

class entregasPageDelete(LoginRequiredMixin,DeleteView):
    template_name = 'entregas_eliminar.html'
    model = entregas
    success_url = reverse_lazy('entregas')
        
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

class almacenPageDelete(LoginRequiredMixin,DeleteView):
    template_name = 'almacen_eliminar.html'
    model = almacen
    success_url = reverse_lazy('almacen')
        
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

class ubicacionPageDelete(LoginRequiredMixin,DeleteView):
    template_name = 'ubicacion_eliminar.html'
    model = ubicacion
    success_url = reverse_lazy('ubicacion')
        
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

#########################################################################
class ComentariosCreateView(LoginRequiredMixin,CreateView):
    template_name = 'agregar_comentario.html'
    model = Comentario
    fields = ('comentario',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.vehiculos_id = self.kwargs['pk']
        return super().form_valid(form)
        ##obligas a la persona que este logeada
   
class ComentariosDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'eliminar_comentario.html'
    model = Comentario
    fields = "__all__"
    success_url = reverse_lazy('vehiculos')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied
        ##obligas a la persona que este logeada
