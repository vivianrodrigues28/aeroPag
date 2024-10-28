from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ClienteForm  
from django.shortcuts import render
from .models import Cliente

# Create
class ClienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    form_class = ClienteForm  
    template_name = 'form.html'
    success_url = reverse_lazy('listar-clientes')

# Update
class ClienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    form_class = ClienteForm  
    template_name = 'form.html'
    success_url = reverse_lazy('listar-clientes')

# Delete
class ClienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

# List
class ClienteList(ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'listas/cliente.html'
