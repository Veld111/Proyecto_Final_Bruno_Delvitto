from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'cuerpo']

    def __init__(self, *args, **kwargs):
        es_respuesta = kwargs.pop('es_respuesta', False)
        super().__init__(*args, **kwargs)
        if es_respuesta:
            self.fields['destinatario'].widget = forms.HiddenInput()
