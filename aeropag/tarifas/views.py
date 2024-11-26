from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Tarifa
from .forms import TarifaForm
from django.http import JsonResponse
from django.contrib import messages



class TarifaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm
    template_name = 'formas.html'
    success_url = reverse_lazy('listar-tarifas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Tarifa criada com sucesso!")
        return super().form_valid(form)

class TarifaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm
    template_name = 'formas.html'
    success_url = reverse_lazy('listar-tarifas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Tarifa atualizada com sucesso!")
        return super().form_valid(form)


class TarifaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tarifa
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-tarifas')

    def get_object(self, queryset=None):
        return get_object_or_404(Tarifa, pk=self.kwargs['pk'], usuario=self.request.user)  

class TarifaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tarifa
    template_name = 'listas/tarifa.html'

    def get_queryset(self):
        return Tarifa.objects.filter(usuario=self.request.user)

