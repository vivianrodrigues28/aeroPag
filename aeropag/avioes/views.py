from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Aviao
from .forms import AviaoForm
# views.py
from django.shortcuts import render
from .models import Aviao

def lista_avioes(request):
    # Filtrando aviões para exibir apenas os do usuário logado
    avioes = Aviao.objects.filter(usuario=request.user)  # Filtra os aviões do usuário logado
    return render(request, 'lista_avioes.html', {'object_list': avioes})


# Função para editar um avião via AJAX
def editar_aviao(request, pk):
    if request.method == 'POST':
        aviao = get_object_or_404(Aviao, pk=pk)
        aviao.prefixo = request.POST.get('prefixo')
        aviao.grupo = request.POST.get('grupo')  # Altere de 'cliente' para 'grupo'
        aviao.toneladas = request.POST.get('toneladas')
        aviao.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

# Função para excluir um avião via AJAX
def excluir_aviao(request, pk):
    if request.method == 'POST':
        aviao = get_object_or_404(Aviao, pk=pk)
        aviao.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

# Classe para criar um novo avião
class AviaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Aviao
    form_class = AviaoForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-avioes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o avião ao usuário logado
        return super().form_valid(form)

# Classe para atualizar os dados de um avião existente
class AviaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Aviao
    form_class = AviaoForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-avioes')

    def get_object(self, queryset=None):
        return get_object_or_404(Aviao, pk=self.kwargs['pk'], usuario=self.request.user)  # Filtra pelo avião do usuário

# Classe para excluir um avião
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
        return Aviao.objects.filter(usuario=self.request.user)  # Exibe apenas os aviões do usuário logado


# Endpoint para fornecer dados via AJAX
def get_avioes(request):
    avioes = Aviao.objects.filter(usuario=request.user).values('prefixo', 'grupo', 'toneladas')  # Alterado para 'grupo'
    return JsonResponse({'avioes': list(avioes)})
