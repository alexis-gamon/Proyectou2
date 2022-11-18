from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

class Ubicacion(models.Model):
    
    Zona = models.CharField(max_length=50)

    CodigoPostal = models.TextField(max_length=10)
## el siguiente comando sirve para que no te aparezca el object en lugar del nombre 
    def __str__(self):
        return self.Zona
#el return debe contener alguna clave de la que se esta haciendo la llave foranea


# Create your models here.
class vehiculos(models.Model):
    Marca = models.TextField(max_length=25)
    Nombre = models.TextField(max_length=25)
    Color =models.TextField(max_length=25)
    Año = models.PositiveIntegerField(null = True, blank = True)
    Disponible = models.TextField(max_length=10)
    
    Ubicacion = models.ForeignKey(
        Ubicacion,
        on_delete=models.CASCADE,
    )
    
    def __str__(self): 
        return self.Marca[:15]

    def get_absolute_url(self):
        return reverse('vehiculos_detalle', args=[str(self.id)])

   
   
class entregas(models.Model):
    Fecha = models.DateTimeField(auto_now_add=True)
    Serie = models.CharField(max_length=10)
    Cliente = models.TextField(max_length=30)
    
    def __str__(self):
        return self.Serie[:15]

class almacen(models.Model):
    NumeroSerie = models.CharField(max_length=30)
    Localidad = models.TextField(max_length=25)
    Lote = models.CharField(max_length=30)
    Fecha = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.Localidad[:15]

class Comentario(models.Model):
    vehiculos = models.ForeignKey(
        vehiculos,
        on_delete=models.CASCADE,
        related_name='comentarios',

    )
    comentario = models.TextField(max_length=200)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('vehiculos')