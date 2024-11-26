from django import forms
from .models import Cobranca, Tarifa

class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'avi_codigo', 'tar_codigo', 'quantidade_horas']
        widgets = {
            'cob_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'avi_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_horas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
tar_codigo = forms.ModelChoiceField(queryset=Tarifa.objects.all(), empty_label="Selecione a Tarifa", widget=forms.Select(attrs={'class': 'form-control'}))
