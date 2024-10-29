from django import forms
from .models import Cliente
from avioes.models import Aviao

class ClienteForm(forms.ModelForm):
    cli_avi_codigo = forms.ModelChoiceField(queryset=Aviao.objects.all(), empty_label="Selecione um avião")

    class Meta:
        model = Cliente
        fields = ['cli_nome', 'cli_email', 'cli_telefone', 'cli_avi_codigo']
        labels = {
            'cli_nome': 'Nome do Cliente',
            'cli_email': 'Email',
            'cli_telefone': 'Telefone',
            'cli_avi_codigo': 'Avião Associado',
        }
