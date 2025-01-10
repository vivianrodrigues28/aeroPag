from django import forms
from .models import Cobranca
from avioes.models import Aviao
from tarifas.models import Tarifa

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'quantidade_horas', 'avi_codigo', 'tar_codigo']
        labels = {
            'cob_codigo': 'Código da Cobrança',
            'quantidade_horas': 'Quantidade de Horas',
            'avi_codigo': 'Código do Avião',
            'tar_codigo': 'Código da Tarifa',
        }
        widgets = {
            'cob_codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o código da cobrança'}),
            'quantidade_horas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Horas de utilização'}),
            'avi_codigo': forms.Select(attrs={'class': 'form-select'}),
            'tar_codigo': forms.Select(attrs={'class': 'form-select'}),
        }
        help_texts = {
            'avi_codigo': 'Selecione o avião relacionado à cobrança.',
            'tar_codigo': 'Escolha a tarifa aplicável.',
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

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'row g-3'
        self.helper.layout = Layout(
            Field('cob_codigo', css_class='col-md-6'),
            Field('quantidade_horas', css_class='col-md-6'),
            Field('avi_codigo', css_class='col-md-6'),
            Field('tar_codigo', css_class='col-md-6'),
            Submit('submit', 'Salvar Cobrança', css_class='btn btn-primary')
        )

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
