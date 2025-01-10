from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cobranca
from .forms import CobrancaForm

# Função para listar as cobranças
def CobrancaList(request):
    cobrancas = Cobranca.objects.all()
    return render(request, 'cobranca/listar.html', {'cobrancas': cobrancas})

# Função para criar uma nova cobrança
def CobrancaCreate(request):
    if request.method == 'POST':
        form = CobrancaForm(request.POST, user=request.user)  # Passando o usuário para o form
        if form.is_valid():
            form.save()
            messages.success(request, "Cobrança criada com sucesso!")
            return redirect('listar_cobrancas')
        else:
            messages.error(request, "Erro ao criar cobrança!")
    else:
        form = CobrancaForm(user=request.user)  # Passando o usuário para o form
    return render(request, 'form_cobranca.html', {'form': form})

# Função para atualizar uma cobrança existente
def CobrancaUpdate(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        form = CobrancaForm(request.POST, instance=cobranca, user=request.user)  # Passando o usuário para o form
        if form.is_valid():
            form.save()
            messages.success(request, "Cobrança atualizada com sucesso!")
            return redirect('listar_cobrancas')
        else:
            messages.error(request, "Erro ao atualizar cobrança!")
    else:
        form = CobrancaForm(instance=cobranca, user=request.user)
    return render(request, 'form_cobranca.html', {'form': form})

# Função para excluir uma cobrança
def CobrancaDelete(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        cobranca.delete()
        messages.success(request, "Cobrança excluída com sucesso!")
        return redirect('listar_cobrancas')
    return render(request, 'confirmar_exclusao.html', {'cobranca': cobranca})


