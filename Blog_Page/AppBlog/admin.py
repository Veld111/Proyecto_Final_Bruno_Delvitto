from django.contrib import admin
from .models import Pelicula, Blog, Mensaje

admin.site.register(Pelicula)
admin.site.register(Mensaje)
admin.site.register(Blog)
