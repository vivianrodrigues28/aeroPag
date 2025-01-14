from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cobranca
from .forms import CobrancaForm


def CobrancaList(request):
    cobrancas = Cobranca.objects.all()
    return render(request, 'cobranca/listar.html', {'cobrancas': cobrancas})


def CobrancaCreate(request):
    if request.method == 'POST':
        form = CobrancaForm(request.POST, user=request.user)  
        if form.is_valid():
            form.save()
            messages.success(request, "Cobrança criada com sucesso!")
            return redirect('listar_cobrancas')
        else:
            messages.error(request, "Erro ao criar cobrança!")
    else:
        form = CobrancaForm(user=request.user)  
    return render(request, 'form_cobranca.html', {'form': form})


def CobrancaUpdate(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        form = CobrancaForm(request.POST, instance=cobranca, user=request.user)  
        if form.is_valid():
            form.save()
            messages.success(request, "Cobrança atualizada com sucesso!")
            return redirect('listar_cobrancas')
        else:
            messages.error(request, "Erro ao atualizar cobrança!")
    else:
        form = CobrancaForm(instance=cobranca, user=request.user)
    return render(request, 'form_cobranca.html', {'form': form})


def CobrancaDelete(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        cobranca.delete()
        messages.success(request, "Cobrança excluída com sucesso!")
        return redirect('listar_cobrancas')
    return render(request, 'confirmar_exclusao.html', {'cobranca': cobranca})


