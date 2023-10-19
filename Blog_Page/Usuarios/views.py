from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from Usuarios.forms import UserEditForm, UserRegisterForm
from .models import UserProfile

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(request, username=usuario, password=contrasenia)

            if user is not None:

                if not hasattr(user, 'userprofile'):
                    UserProfile.objects.create(user=user)

                login(request, user)
                next_url = request.GET.get('next', 'inicio')
                return redirect(next_url)

            msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    # Aquí cambias "users/login.html" por la plantilla que estás utilizando para el inicio de sesión.
    return render(request, "Usuarios/login.html", {"form": form, "msg_login": msg_login})

# Vista de registro
def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return redirect('inicio')
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"Usuarios/registro.html" ,  {"form":form, "msg_register": msg_register})

@login_required
def profile(request):
    return render(request, 'Usuarios/perfil.html')

@login_required
def edit(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            # Verificamos si las contraseñas son iguales
            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                miFormulario = UserEditForm(initial=datos)
            else:
                # Actualizamos los datos del usuario
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()

                messages.success(request, "Perfil actualizado exitosamente!")
                return redirect('inicio')
        else:
            datos = {
                'first_name': usuario.first_name,
                'email': usuario.email
            }
            miFormulario = UserEditForm(initial=datos)
    else:
        datos = {
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "Usuarios/editar.html", {"mi_form": miFormulario, "usuario": usuario})

def logout_request(request):
    logout(request)
    return render(request, "Usuarios/logout.html")

