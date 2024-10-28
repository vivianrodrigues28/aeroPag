from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Tarifa
from .forms import TarifaForm  

# Create
class TarifaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm  
    template_name = 'form.html'
    success_url = reverse_lazy('listar-tarifas')

# Update
class TarifaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm  
    template_name = 'avioes/form.html'  # O caminho do template que você usará para renderizar o formulário
    success_url = 'listas/aviao/'

    def get_object(self, query=None):
        return get_object_or_404(Tarifa, pk=self.kwargs['pk'])


# Delete
class TarifaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tarifa
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-tarifas')

    def get_object(self, query=None):
        return get_object_or_404(Tarifa, pk=self.kwargs['pk'])

# List
class TarifaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tarifa
    template_name = 'listas/tarifa.html'

    def get_queryset(self):
        return Tarifa.objects.all()
