from django.urls import path
from django.views.generic.base import RedirectView
from AppBlog import views

urlpatterns = [
    path('', RedirectView.as_view(url='inicio/', permanent=True)),  # Redirigir la raíz a /inicio/
    path('inicio/', views.inicio, name='inicio'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('categorias/', views.categorias, name='categorias'),
    path('resenas/', views.resenas, name='resenas'),
    path('about/', views.about, name='about'),  # Nueva ruta para la página 'About'
    path('mensajes/', views.mensajes, name='mensajes'),
    path('enviar_mensaje/<int:id_destinatario>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('pages/', views.lista_blogs, name='lista_blogs'),
    path('pages/<int:pageId>/', views.detalle_blog, name='detalle_blog'),
]

