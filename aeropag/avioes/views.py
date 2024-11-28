from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Aviao
from .forms import AviaoForm
from django.shortcuts import render
from .models import Aviao

def listar_avioes(request):
    # Verifica se o usuário está autenticado
    if request.user.is_authenticated:
        avioes = Aviao.objects.filter(usuario=request.user)
    else:
        avioes = Aviao.objects.none()  # Nenhum avião se o usuário não estiver autenticado
    
    return render(request, 'avioes/listar_avioes.html', {'avioes': avioes})


def lista_avioes(request):
    """
    Exibe a lista de aviões cadastrados pelo usuário.
    """
    avioes = Aviao.objects.filter(usuario=request.user).select_related('cliente')
    return render(request, 'lista_avioes.html', {'object_list': avioes})


def editar_aviao(request, pk):
    """
    Edita os dados de um avião específico.
    """
    aviao = get_object_or_404(Aviao, pk=pk)
    if request.method == 'POST':
        form = AviaoForm(request.POST, instance=aviao)
        if form.is_valid():
            form.save()
            messages.success(request, "Avião atualizado com sucesso!")
            return redirect('listar-avioes')  # Substitua pelo nome correto da URL de lista
    else:
        form = AviaoForm(instance=aviao)
    return render(request, 'editar_aviao.html', {'form': form})


def excluir_aviao(request, pk):
    """
    Exclui um avião caso seja uma requisição POST.
    """
    if request.method == 'POST':
        aviao = get_object_or_404(Aviao, pk=pk)
        aviao.delete()
        messages.success(request, "Avião excluído com sucesso!")
    return redirect('listar-avioes')


class AviaoCreate(LoginRequiredMixin, CreateView):
    """
    Cria um novo avião vinculado ao usuário logado.
    """
    login_url = reverse_lazy('login')
    model = Aviao
    form_class = AviaoForm
    template_name = 'forma.html'
    success_url = reverse_lazy('listar-avioes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class AviaoUpdate(LoginRequiredMixin, UpdateView):
    """
    Atualiza um avião específico pertencente ao usuário logado.
    """
    login_url = reverse_lazy('login')
    model = Aviao
    form_class = AviaoForm
    template_name = 'forma.html'
    success_url = reverse_lazy('listar-avioes')

    def get_object(self, queryset=None):
        return get_object_or_404(Aviao, pk=self.kwargs['pk'], usuario=self.request.user)


class AviaoDelete(LoginRequiredMixin, DeleteView):
    """
    Exclui um avião específico pertencente ao usuário logado.
    """
    login_url = reverse_lazy('login')
    model = Aviao
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-avioes')

    def get_object(self, queryset=None):
        return get_object_or_404(Aviao, pk=self.kwargs['pk'], usuario=self.request.user)


class AviaoList(LoginRequiredMixin, ListView):
    """
    Lista os aviões cadastrados pelo usuário logado.
    """
    login_url = reverse_lazy('login')
    model = Aviao
    template_name = 'listas/aviao.html'

    def get_queryset(self):
        return Aviao.objects.filter(usuario=self.request.user)
