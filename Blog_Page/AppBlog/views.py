from django.shortcuts import render
from .models import Pelicula, Resena, Comentario

# Listar todas las películas
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'lista_peliculas.html', {'peliculas': peliculas})

# Detalles de una película específica
def detalles_pelicula(request, pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)
    return render(request, 'detalles_pelicula.html', {'pelicula': pelicula})

# Listar todas las reseñas de una película específica
def lista_resenas(request, pelicula_id):
    resenas = Resena.objects.filter(pelicula_id=pelicula_id)
    return render(request, 'lista_resenas.html', {'resenas': resenas})

# Detalles de una reseña específica
def detalles_resena(request, resena_id):
    resena = Resena.objects.get(id=resena_id)
    return render(request, 'detalles_resena.html', {'resena': resena})

# Listar todos los comentarios de una reseña específica
def lista_comentarios(request, resena_id):
    comentarios = Comentario.objects.filter(resena_id=resena_id)
    return render(request, 'lista_comentarios.html', {'comentarios': comentarios})
