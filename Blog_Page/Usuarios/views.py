from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('iniciar_sesion')
    else:
        formulario = UserCreationForm()
    return render(request, 'Usuarios/registro.html', {'formulario': formulario})



def iniciar_sesion(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['username']
        contraseña = request.POST['password']
        usuario = authenticate(request, username=nombre_usuario, password=contraseña)
        if usuario is not None:
            login(request, usuario)
            return redirect('perfil')
    return render(request, 'Usuarios/iniciar_sesion.html')



@login_required
def perfil(request):
    return render(request, 'Usuarios/perfil.html')



