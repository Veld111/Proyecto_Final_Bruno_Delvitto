from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

def redirect_to_appblog(request):
    return redirect('AppBlog/inicio/')  # Cambia 'AppBlog/inicio/' al nombre de la URL de tu página de inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppBlog/', include('AppBlog.urls')),  # Asegúrate de que ya tienes esto en tu archivo urls.py
    path('Usuarios/', include('Usuarios.urls')),
    path('', redirect_to_appblog),  
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)