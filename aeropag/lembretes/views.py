from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Lembrete
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from datetime import date, timedelta
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone

def cadastrar_lembrete(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        data_str = request.POST.get("data")
        relevancia = request.POST.get("relevancia", 1)
        obs = request.POST.get("obs", "")

        # Converte a data recebida para um objeto 'date'
        data = datetime.strptime(data_str, "%Y-%m-%d").date()

        # Cria e salva o lembrete no banco de dados
        Lembrete.objects.create(
            titulo=titulo,
            descricao=descricao,
            obs=obs,
            relevancia=relevancia,
            data=data,
            usuario=request.user  # Associa o lembrete ao usuário logado
        )

        return redirect('listar_lembretes')  # Redireciona para a página de lista de lembretes

    return render(request, 'cadastro_lembrete.html', {'form': form})


def listar_lembretes(request):
    filtro_data = request.GET.get('filtro_data', 'tudo')
    mensagem = "Todos os lembretes"

    if filtro_data == 'hoje':
        hoje = timezone.now().date()
        lembretes = Lembrete.objects.filter(data=hoje)
        mensagem = "Lembretes de hoje"
    elif filtro_data == 'prox_semana':
        inicio_semana = timezone.now().date() + datetime.timedelta(days=(7 - timezone.now().weekday()))
        fim_semana = inicio_semana + datetime.timedelta(days=6)
        lembretes = Lembrete.objects.filter(data__range=[inicio_semana, fim_semana])
        mensagem = "Lembretes dessa semana"
    elif filtro_data == 'ante_semana':
        inicio_ante_semana = timezone.now().date() - datetime.timedelta(days=(timezone.now().weekday() + 7))
        fim_ante_semana = inicio_ante_semana + datetime.timedelta(days=6)
        lembretes = Lembrete.objects.filter(data__range=[inicio_ante_semana, fim_ante_semana])
        mensagem = "Lembretes da semana passada"
    elif filtro_data == 'ante_tudo':
        lembretes = Lembrete.objects.filter(data__lt=timezone.now().date())
        mensagem = "Lembretes passados"
    elif filtro_data == 'prox_mes':
        primeiro_dia_mes = timezone.now().replace(day=1)
        ultimo_dia_mes = (primeiro_dia_mes.replace(month=primeiro_dia_mes.month + 1) - datetime.timedelta(days=1)).date()
        lembretes = Lembrete.objects.filter(data__range=[primeiro_dia_mes.date(), ultimo_dia_mes])
        mensagem = "Lembretes desse mês"
    else:
        lembretes = Lembrete.objects.all()

    context = {
        'object_list': lembretes,
        'mensagem': mensagem
    }
    return render(request, 'listar_lembretes.html', context)

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
    template_name = 'lembrete/cadastrar_lembrete.html'
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


