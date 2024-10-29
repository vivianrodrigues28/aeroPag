from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ClienteForm  
from django.shortcuts import render
from .models import Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    form_class = ClienteForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-clientes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o cliente ao usuário atual
        return super().form_valid(form)

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    form_class = ClienteForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-clientes')

    def get_object(self, queryset=None):
        return get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)  # Filtra pelo cliente do usuário

class ClienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

    def get_object(self, queryset=None):
        return get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)  # Filtra pelo cliente do usuário

class ClienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'listas/cliente.html'

    def get_queryset(self):
        return Cliente.objects.filter(usuario=self.request.user)  # Lista apenas os clientes do usuário
