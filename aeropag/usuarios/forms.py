from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.core.exceptions import ValidationError
import re
class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email = e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))
        return e




class CadastroForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Este campo é obrigatório.',
            'max_length': 'O nome de usuário deve ter 150 caracteres ou menos.',
        }
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Este campo é obrigatório.',
            'invalid': 'Informe um endereço de e-mail válido.',
        }
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        error_messages={
            'required': 'Este campo é obrigatório.',
            'min_length': 'A senha deve conter pelo menos 8 caracteres.',
        }
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Este campo é obrigatório.',
        }
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if not re.match(r'^[\w@.+/-_]+$', username):
            raise ValidationError('Nome de usuário inválido. Apenas letras, números e @/./+/-/_ são permitidos.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if password.isdigit():
            raise ValidationError('Sua senha não pode ser inteiramente numérica.')
        if password.lower() == self.cleaned_data.get('username', '').lower():
            raise ValidationError('Sua senha não pode ser muito parecida com o nome de usuário.')
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        
        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError('As senhas não coincidem.')
