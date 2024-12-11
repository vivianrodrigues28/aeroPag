from django.contrib.auth.models import User 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Usuário ou senha inválidos."
            print(f"Login failed for user: {username}")  

    print(f"Error message being passed: {error_message}")  
    return render(request, 'login.html', {'error_message': error_message})



#def recuperacao_view(request):
    #return render(request, 'recuperacao.html')

def recuperacao_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Aqui você verifica se o e-mail existe no sistema.
        # Substitua pelo seu modelo de usuário.
        user_exists = User.objects.filter(email=email).exists()
        
        if user_exists:
            send_mail(
                'Recuperação de Senha',
                'Clique no link abaixo para redefinir sua senha:\nhttp://AeroPag.com/password_reset_confirm',
                'noreply@aeropag.com',
                [email],
            )
            messages.success(request, 'Instruções enviadas para o seu e-mail.')
        else:
            messages.error(request, 'E-mail não encontrado.')
            
    return render(request, 'recuperacao.html')


class UsuarioCreate(CreateView):
    model = User 
    form_class = UsuarioForm  
    template_name = 'formr.html'
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

