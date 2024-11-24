from django.contrib.auth.models import User 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.contrib import messages

#def recuperacao_view(request):
    #return render(request, 'recuperacao.html')

def recuperacao_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Aqui você verifica se o e-mail existe no sistema.
        # Substitua pelo seu modelo de usuário.
        user_exists = True  # Exemplo estático; substitua por uma consulta ao banco.
        
        if user_exists:
            send_mail(
                'Recuperação de Senha',
                'Clique no link abaixo para redefinir sua senha:\nhttp://seusite.com/redefinir-senha',
                'noreply@seusite.com',
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
       
        return super().form_valid(form)
