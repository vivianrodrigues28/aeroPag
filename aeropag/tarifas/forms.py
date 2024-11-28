from django import forms
from .models import Tarifa

class TarifaForm(forms.ModelForm):
    class Meta:
        model = Tarifa
        fields = ['tar_tipo', 'tar_valor_domestico', 'tar_valor_internacional', 'tar_grupo', 'tar_ton_min', 'tar_ton_max']
        labels = {
            'tar_tipo': 'Tipo da Tarifa',
            'tar_valor_domestico': 'Valor Doméstico*',
            'tar_valor_internacional': 'Valor Internacional*',
            'tar_grupo': 'Grupo*',
            'tar_ton_min': 'Tonelada Mínima*',
            'tar_ton_max': 'Tonelada Máxima*',
        }

      
