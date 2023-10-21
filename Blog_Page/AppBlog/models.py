from django.contrib.auth.models import User
from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField()
    director = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    imagen = models.ImageField(upload_to='peliculas/')

    def __str__(self):
        return self.titulo

    
class Blog(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, blank=True, null=True)
    cuerpo = models.TextField()  # Campo agregado
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Permitimos valores nulos temporalmente
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='blogs/', null=True, blank=True)


    def __str__(self):
        return self.titulo
