from django import forms
from .models import Cobranca
from avioes.models import Aviao

class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'quantidade_horas', 'valor_total','avi_codigo']

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('user') 
        super().__init__(*args, **kwargs)
