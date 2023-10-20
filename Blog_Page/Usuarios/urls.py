from django.urls import path
from Usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('editar/', views.edit, name='editar'),
    path('perfil/', views.profile, name='perfil'),
]
