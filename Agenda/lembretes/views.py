from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django import forms
from .models import Lembrete

# Create
class LembreteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Lembrete
    fields = ['titulo', 'descricao', 'obs', 'relevancia', 'data']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-lembretes')

    def form_valid(self, form):
        # Verifica se a data é anterior à data atual
        if form.cleaned_data['data'] < timezone.now().date():
            form.add_error('data', 'A data do lembrete não pode ser anterior à data atual.')
            return self.form_invalid(form)
        
        form.instance.usuario = self.request.user
        return super().form_valid(form)

# Update
class LembreteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Lembrete
    fields = ['titulo', 'descricao', 'obs', 'relevancia', 'data']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-lembretes')

    def get_object(self, query=None):
        self.object = get_object_or_404(Lembrete, pk = self.kwargs['pk'], usuario = self.request.user)
        return self.object

# Delete
class LembreteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Lembrete
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-lembretes')

    def get_object(self, query=None):
        self.object = get_object_or_404(Lembrete, pk = self.kwargs['pk'], usuario = self.request.user)
        return self.object

# List
class LembreteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Lembrete
    template_name = 'listas/lembrete.html'

    def get_queryset(self):
        filtro_data = self.request.GET.get('filtro_data', None)

        self.object_list = Lembrete.objects.filter(usuario = self.request.user)

        # ante_tudo ante_semana 
        if filtro_data == 'hoje':
            self.object_list = self.object_list.filter(data=timezone.now().date())
        elif filtro_data == 'prox_semana':
            self.object_list = self.object_list.filter(data__gte=timezone.now(), data__lte=timezone.now() + timezone.timedelta(days=7))
        elif filtro_data == 'prox_mes':
            self.object_list = self.object_list.filter(data__gte=timezone.now(), data__lte=timezone.now() + timezone.timedelta(days=30))
        elif filtro_data == 'ante_semana':
            self.object_list = self.object_list.filter(data__lte=timezone.now(), data__gte=timezone.now() - timezone.timedelta(days=7))
        elif filtro_data == 'ante_tudo':
            self.object_list = self.object_list.filter(data__lte=timezone.now())
        
        elif filtro_data == 'tudo':
            # Não filtra
            self.object_list
        else:
            self.object_list = self.object_list.filter(data__gte=timezone.now(), data__lte=timezone.now() + timezone.timedelta(days=7))

        return self.object_list