from django import forms
from .models import Aviao

class AviaoForm(forms.ModelForm):
    class Meta:
        model = Aviao
        fields = ['avi_prefixo_do_aviao', 'avi_grupo', 'avi_toneladas']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Recupera o usuário logado
        super().__init__(*args, **kwargs)

        if user:
            # Filtra os aviões do usuário logado
            self.fields['avi_grupo'].queryset = Aviao.objects.filter(usuario=user)
