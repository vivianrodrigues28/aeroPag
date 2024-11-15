from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Lembrete
from django.contrib.auth.decorators import login_required
# lembretes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lembrete
from django.http import JsonResponse
from .models import Lembrete
def listar_lembretes(request):
    lembretes = Lembrete.objects.all()

    lembretes = lembretes.order_by('data')

    return render(request, 'lembrete.html', {'object_list': lembretes})
def editar_lembrete(request, id):
    if request.method == 'POST':
        lembrete = Lembrete.objects.get(id=id)
        titulo = request.POST.get('titulo')
        obs = request.POST.get('obs')
        lembrete.titulo = titulo
        lembrete.obs = obs
        lembrete.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)


def excluir_lembrete(request, id):
    # Obtém o lembrete com base no ID fornecido
    lembrete = get_object_or_404(Lembrete, pk=id)

    # Exclui o lembrete
    lembrete.delete()

    # Redireciona para a lista de lembretes após a exclusão
    return redirect('listar-lembretes')

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


