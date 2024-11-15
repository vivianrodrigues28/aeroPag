from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Tarifa
from .forms import TarifaForm
from django.http import JsonResponse


def listar_tarifas(request):
    # Filtra as tarifas do usuário logado
    tarifas = Tarifa.objects.filter(usuario=request.user)
    return render(request, 'lista_tarifas.html', {'tarifas': tarifas})


def criar_tarifa(request):
    if request.method == 'POST':
        form = TarifaForm(request.POST)
        if form.is_valid():
            tarifa = form.save(commit=False)
            tarifa.usuario = request.user  # Associa a tarifa ao usuário atual
            tarifa.save()
            # Retorna os dados da tarifa recém-criada para atualizar a tabela via AJAX
            return JsonResponse({
                'pk': tarifa.pk,
                'descricao': tarifa.descricao,
                'valor': tarifa.valor,
            })
    else:
        form = TarifaForm()
    return render(request, 'cadastrar_tarifa.html', {'form': form})


def excluir_tarifa(request, tarifa_id):
    if request.method == 'POST':
        try:
            tarifa = Tarifa.objects.get(pk=tarifa_id, usuario=request.user)
            tarifa.delete()
            return JsonResponse({'status': 'success'})
        except Tarifa.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Tarifa não encontrada'}, status=404)


def editar_tarifa(request, tarifa_id):
    if request.method == 'POST':
        tarifa = get_object_or_404(Tarifa, pk=tarifa_id)
        tarifa.tar_tipo = request.POST.get('tipo')
        tarifa.tar_valor_domestico = request.POST.get('valor_domestico')
        tarifa.tar_valor_internacional = request.POST.get('valor_internacional')
        tarifa.tar_grupo = request.POST.get('grupo')
        tarifa.tar_ton_min = request.POST.get('ton_min')
        tarifa.tar_ton_max = request.POST.get('ton_max')
        tarifa.save()

        # Resposta JSON com os dados atualizados
        return JsonResponse({
            'status': 'success',
            'tipo': tarifa.tar_tipo,
            'valor_domestico': tarifa.tar_valor_domestico,
            'valor_internacional': tarifa.tar_valor_internacional,
            'grupo': tarifa.tar_grupo,
            'ton_min': tarifa.tar_ton_min,
            'ton_max': tarifa.tar_ton_max
        })
    return JsonResponse({'status': 'error', 'message': 'Método inválido'}, status=400)


class TarifaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-tarifas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa a tarifa ao usuário atual
        return super().form_valid(form)


class TarifaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-tarifas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)



class TarifaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tarifa
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-tarifas')

    def get_object(self, queryset=None):
        return get_object_or_404(Tarifa, pk=self.kwargs['pk'], usuario=self.request.user)  # Filtra pela tarifa do usuário


class TarifaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tarifa
    template_name = 'listas/tarifa.html'

    def get_queryset(self):
        # Lista apenas as tarifas do usuário logado
        return Tarifa.objects.filter(usuario=self.request.user)

