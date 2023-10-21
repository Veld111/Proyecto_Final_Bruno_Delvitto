from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.lista_mensajes, name='lista_mensajes'),
    path('messages/send/', views.enviar_mensaje, name='enviar_mensaje'),
    path('messages/<int:id>/', views.ver_mensaje, name='ver_mensaje'),
]
