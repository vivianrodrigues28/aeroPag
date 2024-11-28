from django import forms
from .models import Cobranca
from avioes.models import Aviao

class CobrancaForm(forms.ModelForm):
    class Meta:
        model = Cobranca
        fields = ['cob_codigo', 'quantidade_horas', 'valor_total', 'avi_codigo']
    
    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        self.usuario = kwargs.pop('user', None)  # Evita KeyError
        super().__init__(*args, **kwargs)

        # Exemplo de como filtrar um campo com base no usuário
        if self.usuario:
            self.fields['avi_codigo'].queryset = Aviao.objects.filter(usuario=self.usuario)
=======
            super().__init__(*args, **kwargs)
        # Filtra os aviões cadastrados pelo usuário logado (se necessário)
            self.fields['avi_codigo'].queryset = Aviao.objects.all()
     
>>>>>>> b17d301ab4a8a810ee75e581beebafbb8aa10dcd
