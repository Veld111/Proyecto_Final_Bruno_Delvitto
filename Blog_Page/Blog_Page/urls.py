from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def redirect_to_appblog(request):
    return redirect('inicio')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppBlog/', include('AppBlog.urls')),
    path('Usuarios/', include('Usuarios.urls')),
    path('', redirect_to_appblog),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
