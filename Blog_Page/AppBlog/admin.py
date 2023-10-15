from django.contrib import admin
from .models import Pelicula, Resena, Comentario, Blog, Mensaje

admin.site.register(Pelicula)
admin.site.register(Resena)
admin.site.register(Comentario)
admin.site.register(Mensaje)
admin.site.register(Blog)
