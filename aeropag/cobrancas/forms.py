from django import forms
from .models import Cobranca
from avioes.models import Aviao
from tarifas.models import Tarifa


class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'avi_codigo', 'tar_codigo', 'quantidade_horas', 'valor_total']
        widgets = {
            'valor_total': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.usuario:
            self.fields['avi_codigo'].queryset = Aviao.objects.filter(usuario=self.usuario)
            self.fields['tar_codigo'].queryset = Tarifa.objects.filter(usuario=self.usuario)
        else:
            self.fields['avi_codigo'].queryset = Aviao.objects.none()
            self.fields['tar_codigo'].queryset = Tarifa.objects.none()

