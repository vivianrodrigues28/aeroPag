from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm

class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')