from django.shortcuts import render
from .models import Pelicula, Resena, Comentario

from django.shortcuts import render

def inicio(request):
    return render(request, 'AppBlog/index.html')

def peliculas(request):
    return render(request, 'AppBlog/peliculas.html')

def categorias(request):
    return render(request, 'AppBlog/categorias.html')

def resenas(request):
    return render(request, 'AppBlog/resenas.html')

def about(request):  # Nueva función de vista para la página 'About'
    return render(request, 'AppBlog/about.html')


