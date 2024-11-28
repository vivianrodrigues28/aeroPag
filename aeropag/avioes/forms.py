from django import forms
from .models import Aviao

class AviaoForm(forms.ModelForm):
    class Meta:
        model = Aviao
        fields = ['avi_prefixo_do_aviao', 'avi_toneladas', 'avi_grupo']
        labels = {
            'avi_prefixo_do_aviao': 'Prefixo do Avião',
            'avi_toneladas': 'Toneladas',
            'avi_grupo': 'Grupo',
        }
