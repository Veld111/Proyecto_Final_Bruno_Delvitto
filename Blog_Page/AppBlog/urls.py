from django.urls import path
from . import views

urlpatterns = [
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('peliculas/<int:pelicula_id>/', views.detalles_pelicula, name='detalles_pelicula'),
    path('peliculas/<int:pelicula_id>/resenas/', views.lista_resenas, name='lista_resenas'),
    path('resenas/<int:resena_id>/', views.detalles_resena, name='detalles_resena'),
    path('resenas/<int:resena_id>/comentarios/', views.lista_comentarios, name='lista_comentarios'),
]