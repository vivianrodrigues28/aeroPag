from django import forms
from .models import Cobranca

class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'tar_cod', 'quantidade_horas','avi_codigo']
