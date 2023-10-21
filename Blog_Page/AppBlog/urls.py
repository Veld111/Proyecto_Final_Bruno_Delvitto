from django.urls import path
from django.views.generic.base import RedirectView
from AppBlog import views

urlpatterns = [
    path('', RedirectView.as_view(url='inicio/', permanent=True)),  # Redirigir la raíz a /inicio/
    path('inicio/', views.inicio, name='inicio'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('about/', views.about, name='about'),  # Nueva ruta para la página 'About'mensaje/<int:id_destinatario>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('pages/', views.lista_blogs, name='lista_blogs'),
    path('pages/<int:pageId>/', views.detalle_blog, name='detalle_blog'),
    path('blog/editar/<int:blog_id>/', views.editar_blog, name='editar_blog'),
    path('blog/borrar/<int:blog_id>/', views.borrar_blog, name='borrar_blog'),
]


