from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')
    cuerpo = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
