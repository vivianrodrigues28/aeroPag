from django import forms
from .models import Cobranca
from avioes.models import Aviao


class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'quantidade_horas', 'valor_total', 'avi_codigo']
    
    def __init__(self, *args, **kwargs):
        """
        Inicializa o formulário e, se fornecido um usuário, filtra os aviões cadastrados por ele.
        """
        self.usuario = kwargs.pop('user', None)  # Evita KeyError ao remover 'user' dos kwargs
        super().__init__(*args, **kwargs)

        # Filtra o campo 'avi_codigo' baseado no usuário, se fornecido
        if self.usuario:
            self.fields['avi_codigo'].queryset = Aviao.objects.filter(usuario=self.usuario)
        else:
            self.fields['avi_codigo'].queryset = Aviao.objects.none()
