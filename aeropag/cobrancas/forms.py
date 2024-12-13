from django import forms
from .models import Cobranca
from avioes.models import Aviao
from tarifas.models import Tarifa


class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'quantidade_horas', 'avi_codigo', 'tar_codigo']


    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.usuario:
            self.fields['avi_codigo'].queryset = Aviao.objects.filter(usuario=self.usuario)
            self.fields['tar_codigo'].queryset = Tarifa.objects.filter(usuario=self.usuario)
        else:
            self.fields['avi_codigo'].queryset = Aviao.objects.none()
            self.fields['tar_codigo'].queryset = Tarifa.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        avi_codigo = cleaned_data.get('avi_codigo')
        tar_codigo = cleaned_data.get('tar_codigo')
        quantidade_horas = cleaned_data.get('quantidade_horas')

        if avi_codigo and tar_codigo:
            # Realiza o cálculo com base no tipo de tarifa e as informações do avião
            if avi_codigo.avi_toneladas < tar_codigo.tar_ton_min or avi_codigo.avi_toneladas > tar_codigo.tar_ton_max:
                raise forms.ValidationError("O peso do avião está fora da faixa da tarifa selecionada.")

        return cleaned_data
