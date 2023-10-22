from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')
    asunto = models.CharField(max_length=255, null=True, blank=True)
    cuerpo = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.remitente} para {self.destinatario}"