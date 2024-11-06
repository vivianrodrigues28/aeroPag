from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Lembrete

class LembreteCreate(LoginRequiredMixin, CreateView):
    model = Lembrete
    fields = ['titulo', 'descricao', 'obs', 'relevancia', 'data']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-lembretes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associando o lembrete ao usuário logado
        return super().form_valid(form)

class LembreteUpdate(LoginRequiredMixin, UpdateView):
    model = Lembrete
    fields = ['titulo', 'descricao', 'obs', 'relevancia', 'data']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-lembretes')

    def get_object(self):
        return get_object_or_404(Lembrete, pk=self.kwargs['pk'], usuario=self.request.user)

class LembreteDelete(LoginRequiredMixin, DeleteView):
    model = Lembrete
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-lembretes')

    def get_object(self):
        return get_object_or_404(Lembrete, pk=self.kwargs['pk'], usuario=self.request.user)

class LembreteList(LoginRequiredMixin, ListView):
    model = Lembrete
    template_name = 'listas/lembrete.html'

    def get_queryset(self):
        return Lembrete.objects.filter(usuario=self.request.user)  # Filtrando pelos lembretes do usuário logado


