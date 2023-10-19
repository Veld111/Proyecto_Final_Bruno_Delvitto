from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import BlogForm
from .models import Pelicula, Blog

# Comprobar si el usuario es administrador
def es_admin(user):
    return user.is_staff


@login_required
@user_passes_test(es_admin)
def editar_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('detalle_blog', pageId=blog_id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'AppBlog/editar_blog.html', {'form': form, 'blog': blog})

@login_required
@user_passes_test(es_admin)
def borrar_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect('lista_blogs')
    return render(request, 'AppBlog/confirmar_borrado.html', {'blog': blog})


@login_required
@user_passes_test(es_admin)
def crear_blog(request):
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



def detalle_blog(request, pageId):
    blog = get_object_or_404(Blog, id=pageId)
    return render(request, 'AppBlog/detalle_blog.html', {'blog': blog})

def lista_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'AppBlog/lista_blogs.html', {'blogs': blogs})


def inicio(request):
    blogs = Blog.objects.all()  
    return render(request, 'AppBlog/index.html', {'blogs': blogs})

def peliculas(request):
    return render(request, 'AppBlog/peliculas.html')

def categorias(request):
    return render(request, 'AppBlog/categorias.html')

def resenas(request):
    return render(request, 'AppBlog/resenas.html')

def about(request):  # Nueva función de vista para la página 'About'
    return render(request, 'AppBlog/about.html')


