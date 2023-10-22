from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import AvatarUploadForm
from .models import UserProfile
from Usuarios.forms import UserEditForm, UserRegisterForm
from django.contrib.auth.models import User
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
    print("Vista de perfil accedida")  # Para confirmar que la vista se accede correctamente

    if request.method == 'POST':
        print("Se recibió una solicitud POST")

        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid():
            form.save()
            return redirect('perfil')  # redirige de nuevo al perfil tras guardar
    else:
        print("Solicitud GET o de otro tipo")
        form = AvatarUploadForm(instance=request.user.userprofile)
    
    perfil = request.user.userprofile
    es_mismo_usuario = True
    context = {
        'form': form,
        'usuario': request.user,
        'perfil': perfil,
        'es_mismo_usuario': es_mismo_usuario
    }
    return render(request, 'Usuarios/perfil.html', context)



def ver_perfil(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    perfil = usuario.userprofile
    
    # Verificar si el usuario actualmente autenticado es el mismo que el usuario del perfil.
    es_mismo_usuario = False
    if request.user == usuario:
        es_mismo_usuario = True

    return render(request, 'Usuarios/perfil.html', {'usuario': usuario, 'perfil': perfil, 'es_mismo_usuario': es_mismo_usuario})


@login_required
def edit(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

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

                # Código para guardar el avatar si ha sido modificado
                perfil = usuario.userprofile
                if 'avatar' in miFormulario.changed_data:
                    perfil.avatar = informacion['avatar']
                if 'descripcion' in miFormulario.changed_data:
                    perfil.descripcion = informacion['descripcion']
                if 'web_url' in miFormulario.changed_data:
                    perfil.web_url = informacion['web_url']
                perfil.save()

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

