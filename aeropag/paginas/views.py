from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from avioes.models import Aviao
from lembretes.models import Lembrete
from clientes.models import Cliente
from tarifas.models import Tarifa
from django.shortcuts import render
# views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Lembrete
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Lembrete
# Exemplo de uma view que passa o total de lembretes para o template


def listar_lembretes(request):
    filtro_data = request.GET.get('filtro_data', 'tudo')
    
    # Definir a data inicial de comparação
    hoje = datetime.today().date()
    inicio_semana = hoje - timedelta(days=hoje.weekday())  # Início da semana (segunda-feira)
    fim_semana = inicio_semana + timedelta(days=6)  # Fim da semana (domingo)
    inicio_mes = hoje.replace(day=1)  # Primeiro dia do mês
    fim_mes = hoje.replace(month=hoje.month + 1, day=1) - timedelta(days=1)  # Último dia do mês

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
    elif filtro_data == 'tudo':
        lembretes = Lembrete.objects.all()
    else:
        lembretes = Lembrete.objects.all()

    return render(request, 'listar_lembretes.html', {'lembretes': lembretes})

def excluir_lembrete(request, id):
    if request.method == "POST":
        lembrete = get_object_or_404(Lembrete, id=id)
        lembrete.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

# Função de visualização para o dashboard
def dashboard(request):
    total_avioes = Aviao.objects.count()
    lista_avioes = Aviao.objects.all()
    lista_clientes = Cliente.objects.all()
    total_clientes = lista_clientes.count()
    total_tarifas = Tarifa.objects.count()  # Conta o total de tarifas
    lista_tarifas = Tarifa.objects.all() 
    total_lembretes = Lembrete.objects.count()
    lista_lembretes = Lembrete.objects.all()
    
    context = {
        'total_avioes': total_avioes,
        'lista_avioes': lista_avioes,
        'total_lembretes': total_lembretes,
        'lista_lembretes': lista_lembretes,
        'lista_clientes': lista_clientes,  # Certifique-se de que 'lista_clientes' está sendo passado aqui
        'total_clientes': total_clientes,
        'total_tarifas': total_tarifas,
        'lista_tarifas': lista_tarifas,
    

    }
    return render(request, 'paginas/dashboard.html', context)

# Classe baseada em template para o dashboard
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona aviões e lembretes ao contexto
        context['total_avioes'] = Aviao.objects.count()
        context['lista_avioes'] = Aviao.objects.all()
        context['total_lembretes'] = Lembrete.objects.count()  # Adiciona a contagem de lembretes
        context['lista_lembretes'] = Lembrete.objects.all()  
        context['lista_clientes'] = Cliente.objects.all()
        context['total_clientes'] = Cliente.objects.count()
        context['lista_tarifas'] = Tarifa.objects.all()
        context['total_tarifas'] = Tarifa.objects.count()
        
 

       
        return context

# Classe para a view da página inicial
class IndexView(TemplateView):
    login_url = reverse_lazy('login')
    template_name = "index.html"
