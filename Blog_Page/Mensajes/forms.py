from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'cuerpo']  # Agregar el campo 'asunto' a la lista de campos.

    def __init__(self, *args, **kwargs):
        super(MensajeForm, self).__init__(*args, **kwargs)
        self.fields['asunto'].widget.attrs.update({
            'class': 'form-control',
            'style': 'width:50%;'
        })

