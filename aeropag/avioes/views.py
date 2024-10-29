from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Aviao
from .forms import AviaoForm  

class AviaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Aviao
    form_class = AviaoForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-avioes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o avião ao usuário atual
        return super().form_valid(form)

class AviaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Aviao
    form_class = AviaoForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-avioes')

    def get_object(self, queryset=None):
        return get_object_or_404(Aviao, pk=self.kwargs['pk'], usuario=self.request.user)  # Filtra pelo avião do usuário

class AviaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Aviao
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-avioes')

    def get_object(self, queryset=None):
        return get_object_or_404(Aviao, pk=self.kwargs['pk'], usuario=self.request.user)  # Filtra pelo avião do usuário

class AviaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Aviao
    template_name = 'listas/aviao.html'

    def get_queryset(self):
        return Aviao.objects.filter(usuario=self.request.user)  # Lista apenas os aviões do usuário
