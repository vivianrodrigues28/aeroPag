from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from avioes.models import Aviao
from lembretes.models import Lembrete
from clientes.models import Cliente
from tarifas.models import Tarifa
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from datetime import datetime, timedelta
# View para a busca
def search(request):
    query = request.GET.get('query', '')  # Obtém a consulta da barra de pesquisa
    
    if query:
        results = Aviao.objects.filter(nome__icontains=query)  # Filtra pelo campo 'nome'
    else:
        results = Aviao.objects.all()  # Se não houver consulta, retorna todos os registros
    
    return render(request, 'search_results.html', {'query': query, 'results': results})

# View para listar lembretes com filtros de data
def listar_lembretes(request):
    filtro_data = request.GET.get('filtro_data', 'tudo')
    hoje = datetime.today().date()
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timedelta(days=6)
    inicio_mes = hoje.replace(day=1)
    fim_mes = (inicio_mes.replace(month=inicio_mes.month + 1) - timedelta(days=1)) if inicio_mes.month < 12 else datetime(hoje.year + 1, 1, 1) - timedelta(days=1)

    if filtro_data == 'hoje':
        lembretes = Lembrete.objects.filter(data__date=hoje)
    elif filtro_data == 'prox_semana':
        lembretes = Lembrete.objects.filter(data__date__range=[inicio_semana, fim_semana])
    elif filtro_data == 'ante_semana':
        semana_passada_inicio = inicio_semana - timedelta(days=7)
        semana_passada_fim = fim_semana - timedelta(days=7)
        lembretes = Lembrete.objects.filter(data__date__range=[semana_passada_inicio, semana_passada_fim])
    elif filtro_data == 'ante_tudo':
        lembretes = Lembrete.objects.filter(data__date__lt=hoje)
    elif filtro_data == 'prox_mes':
        lembretes = Lembrete.objects.filter(data__date__range=[inicio_mes, fim_mes])
    else:
        lembretes = Lembrete.objects.all()

    return render(request, 'listar_lembretes.html', {'lembretes': lembretes})

# View para excluir lembrete via AJAX
def excluir_lembrete(request, id):
    if request.method == "POST":
        lembrete = get_object_or_404(Lembrete, id=id)
        lembrete.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
def excluir_aviao(request, aviao_id):
    if request.method == "POST":
        aviao = get_object_or_404(Aviao, pk=aviao_id)
        aviao.delete()
        return JsonResponse({'status': 'sucesso'})
    return JsonResponse({'status': 'erro'}, status=400)

def excluir_cliente(request, id):
    if request.method == "POST":
        cliente = get_object_or_404(Cliente, id=id)
        cliente.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def excluir_tarifa(request, id):
    if request.method == "POST":
        tarifa = get_object_or_404(Tarifa, id=id)
        tarifa.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

# View para o dashboard
def dashboard(request):
    total_avioes = Aviao.objects.count()
    lista_avioes = Aviao.objects.all()
    lista_clientes = Cliente.objects.all()
    total_clientes = lista_clientes.count()
    total_tarifas = Tarifa.objects.count()
    lista_tarifas = Tarifa.objects.all()
    total_lembretes = Lembrete.objects.count()
    lista_lembretes = Lembrete.objects.all()
    
    context = {
        'total_avioes': total_avioes,
        'lista_avioes': lista_avioes,
        'total_lembretes': total_lembretes,
        'lista_lembretes': lista_lembretes,
        'lista_clientes': lista_clientes,
        'total_clientes': total_clientes,
        'total_tarifas': total_tarifas,
        'lista_tarifas': lista_tarifas,
    }
    return render(request, 'paginas/dashboard.html', context)

# Dashboard com classe baseada em TemplateView
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_avioes'] = Aviao.objects.count()
        context['lista_avioes'] = Aviao.objects.all()
        context['total_lembretes'] = Lembrete.objects.count()
        context['lista_lembretes'] = Lembrete.objects.all()
        context['lista_clientes'] = Cliente.objects.all()
        context['total_clientes'] = Cliente.objects.count()
        context['lista_tarifas'] = Tarifa.objects.all()
        context['total_tarifas'] = Tarifa.objects.count()
        return context

# View para a página inicial
class IndexView(TemplateView):
    login_url = reverse_lazy('login')
    template_name = "index.html"
