from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Turma, Atividade
from django.views.generic.list import ListView

# Create
class TurmaCreate(CreateView):
    model = Turma
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-turmas')
class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'turma']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-turmas')

# Update
class TurmaUpdate(UpdateView):
    model = Turma
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-turmas')
class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'turma']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-turmas')


# Delete
class TurmaDelete(DeleteView):
    model = Turma
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-turmas')
class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-turmas')


# List
class TurmaList(ListView):
    model = Turma
    template_name = 'listas/turma.html'

class AtividadeList(ListView):
    model = Atividade
    template_name = 'listas/atividade.html'