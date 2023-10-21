from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_mensajes(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'Mensajes/lista_mensajes.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('lista_mensajes')
    else:
        form = MensajeForm()
    return render(request, 'Mensajes/enviar_mensaje.html', {'form': form})

@login_required
def ver_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    return render(request, 'Mensajes/ver_mensaje.html', {'mensaje': mensaje})
