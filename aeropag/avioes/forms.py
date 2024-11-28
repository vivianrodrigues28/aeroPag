from django import forms
from .models import Aviao
from clientes.models import Cliente

class AviaoForm(forms.ModelForm):
    class Meta:
        model = Aviao
        fields = ['avi_prefixo_do_aviao', 'avi_toneladas', 'cli_nome']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        # Filtra os aviões cadastrados pelo usuário logado (se necessário)
            self.fields['cli_nome'].queryset = Cliente.objects.all()
     
