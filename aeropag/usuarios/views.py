from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.shortcuts import render  # Adicione essa linha para importar render

def recuperacao_view(request):
    return render(request, 'recuperacao.html')  # Agora a função render está disponível

class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')