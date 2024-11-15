from django import forms

class LembreteForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    descricao = forms.CharField(widget=forms.Textarea)
    observacoes = forms.CharField(widget=forms.Textarea)
    grau_relevancia = forms.ChoiceField(choices=[(1, 'Alta'), (2, 'Média'), (3, 'Baixa')])
    data = forms.DateField(widget=forms.SelectDateWidget)
