from django import forms
from .models import Cobranca

from django import forms
from .models import Cobranca

class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'avi_codigo', 'tar_codigo', 'quantidade_horas']
        widgets = {
            'cob_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'avi_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_horas': forms.NumberInput(attrs={'class': 'form-control'}),
        }

