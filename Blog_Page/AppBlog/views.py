from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Resena, Comentario, Blog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


def detalle_blog(request, pageId):
    blog = get_object_or_404(Blog, id=pageId)
    return render(request, 'detalle_blog.html', {'blog': blog})

def lista_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'lista_blogs.html', {'blogs': blogs})


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


# Comprobar si el usuario es administrador
def es_admin(user):
    return user.is_staff

@login_required
@user_passes_test(es_admin)
def crear_pelicula(request):
    pass
    # Tu lógica para crear una película


@login_required
def mensajes(request):
    pass
    # Tu lógica para mostrar mensajes

@login_required
def enviar_mensaje(request, id_destinatario):
    pass
    # Tu lógica para enviar un nuevo mensaje
