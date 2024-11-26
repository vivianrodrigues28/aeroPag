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
from django.contrib.auth.decorators import login_required

def search(request):
    query = request.GET.get('query', '')  
    
    if query:
        results = Aviao.objects.filter(nome__icontains=query)  
    else:
        results = Aviao.objects.all()  
    
    return render(request, 'search_results.html', {'query': query, 'results': results})


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


@login_required
def dashboard(request):
    user = request.user  
    total_avioes = Aviao.objects.filter(usuario=user).count() if Aviao.objects.filter(usuario=user).exists() else 0
    lista_avioes = Aviao.objects.filter(usuario=user) if Aviao.objects.filter(usuario=user).exists() else []

    total_clientes = Cliente.objects.filter(usuario=user).count() if Cliente.objects.filter(usuario=user).exists() else 0
    lista_clientes = Cliente.objects.filter(usuario=user) if Cliente.objects.filter(usuario=user).exists() else []

    total_tarifas = Tarifa.objects.filter(usuario=user).count() if Tarifa.objects.filter(usuario=user).exists() else 0
    lista_tarifas = Tarifa.objects.filter(usuario=user) if Tarifa.objects.filter(usuario=user).exists() else []

    total_lembretes = Lembrete.objects.filter(usuario=user).count() if Lembrete.objects.filter(usuario=user).exists() else 0
    lista_lembretes = Lembrete.objects.filter(usuario=user) if Lembrete.objects.filter(usuario=user).exists() else []

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

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user 
        context['total_avioes'] = Aviao.objects.filter(usuario=user).count() if Aviao.objects.filter(usuario=user).exists() else 0
        context['lista_avioes'] = Aviao.objects.filter(usuario=user) if Aviao.objects.filter(usuario=user).exists() else []

        context['total_lembretes'] = Lembrete.objects.filter(usuario=user).count() if Lembrete.objects.filter(usuario=user).exists() else 0
        context['lista_lembretes'] = Lembrete.objects.filter(usuario=user) if Lembrete.objects.filter(usuario=user).exists() else []

        context['total_clientes'] = Cliente.objects.filter(usuario=user).count() if Cliente.objects.filter(usuario=user).exists() else 0
        context['lista_clientes'] = Cliente.objects.filter(usuario=user) if Cliente.objects.filter(usuario=user).exists() else []

        context['total_tarifas'] = Tarifa.objects.filter(usuario=user).count() if Tarifa.objects.filter(usuario=user).exists() else 0
        context['lista_tarifas'] = Tarifa.objects.filter(usuario=user) if Tarifa.objects.filter(usuario=user).exists() else []

        return context


class IndexView(TemplateView):
    login_url = reverse_lazy('login')
    template_name = "index.html"
