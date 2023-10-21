from django.urls import path
from . import views

urlpatterns = [
    path('lista_mensaje/', views.lista_mensajes, name='lista_mensajes'),
    path('enviar_mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    path('enviar_mensaje/<int:respuesta_a_id>/', views.enviar_mensaje, name='responder_mensaje'),
    path('ver_mensaje/<int:id_mensaje>/', views.ver_mensaje, name='ver_mensaje'),
]
