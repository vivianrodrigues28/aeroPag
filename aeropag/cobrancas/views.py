from django.shortcuts import render, get_object_or_404, redirect
from .models import Cobranca
from .forms import CobrancaForm

#listar cobrança
def listar_cobrancas(request):
    cobrancas = Cobranca.objects.all()
    return render(request, 'cobrancas/listar.html', {'cobrancas': cobrancas})

# Criar cobrança
def criar_cobranca(request):
    if request.method == 'POST':
        form = CobrancaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cobrancas')
    else:
        form = CobrancaForm()
    return render(request, 'cobrancas/form.html', {'form': form})

# Editar cobrança
def editar_cobranca(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        form = CobrancaForm(request.POST, instance=cobranca)
        if form.is_valid():
            form.save()
            return redirect('listar_cobrancas')
    else:
        form = CobrancaForm(instance=cobranca)
    return render(request, 'cobrancas/form.html', {'form': form})

# Excluir cobrança
def excluir_cobranca(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        cobranca.delete()
        return redirect('listar_cobrancas')
    return render(request, 'cobrancas/confirmar_exclusao.html', {'cobranca': cobranca})

# Create your views here.
