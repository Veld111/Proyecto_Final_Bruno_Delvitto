from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_appblog(request):
    return redirect('AppBlog/inicio/')  # Cambia 'AppBlog/inicio/' al nombre de la URL de tu página de inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppBlog/', include('AppBlog.urls')),  # Asegúrate de que ya tienes esto en tu archivo urls.py
    path('', redirect_to_appblog),
]