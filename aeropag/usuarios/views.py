from django.contrib.auth.models import User 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.contrib.auth.forms import UserCreationForm

def recuperacao_view(request):
    return render(request, 'recuperacao.html')

class UsuarioCreate(CreateView):
    model = User 
    form_class = UsuarioForm  
    template_name = 'formr.html'
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
       
        return super().form_valid(form)
