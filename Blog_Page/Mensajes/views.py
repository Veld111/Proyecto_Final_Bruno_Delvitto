from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_mensajes(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'Mensajes/lista_mensajes.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request, respuesta_a_id=None):
    if respuesta_a_id:
        mensaje_original = Mensaje.objects.get(id=respuesta_a_id)
        if request.method == "POST":
            form = MensajeForm(request.POST)
            if form.is_valid():
                mensaje = form.save(commit=False)
                mensaje.remitente = request.user
                mensaje.save()
                return redirect('lista_mensajes')
        else:
            form = MensajeForm(initial={'destinatario': mensaje_original.remitente})
    else:
        if request.method == "POST":
            form = MensajeForm(request.POST)
            if form.is_valid():
                mensaje = form.save(commit=False)
                mensaje.remitente = request.user
                mensaje.save()
                return redirect('lista_mensajes')
        else:
            form = MensajeForm()

    return render(request, 'Mensajes/enviar_mensaje.html', {'form': form, 'respuesta_a_id': respuesta_a_id})




@login_required
def ver_mensaje(request, id_mensaje):
    mensaje = get_object_or_404(Mensaje, pk=id_mensaje)
    return render(request, 'Mensajes/ver_mensaje.html', {'mensaje': mensaje})

