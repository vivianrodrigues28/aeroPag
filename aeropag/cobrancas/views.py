from django.shortcuts import render, get_object_or_404, redirect
from .models import Cobranca, Aviao, Tarifa
from .forms import CobrancaForm

def CobrancaList(request):
    cobrancas = Cobranca.objects.all()  # Busca todas as cobranças
    return render(request, 'cobranca_list.html', {'cobrancas': cobrancas})


def CobrancaCreate(request):
    avioes = Aviao.objects.all()  # Busca todos os aviões
    tarifas = Tarifa.objects.all()  # Busca todas as tarifas

    if request.method == 'POST':
        form = CobrancaForm(request.POST)
        if form.is_valid():
            cobranca = form.save(commit=False)
            cobranca.save()
            return redirect('listar_cobrancas')
    else:
        form = CobrancaForm()
<<<<<<< HEAD
=======
    
    return render(request, 'formc.html', {'form': form})
>>>>>>> b17d301ab4a8a810ee75e581beebafbb8aa10dcd

    return render(request, 'formc.html', {
        'form': form,
        'avioes': avioes,  # Passando aviões para o template
        'tarifas': tarifas  # Passando tarifas para o template
    })


def CobrancaUpdate(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    avioes = Aviao.objects.all()  # Busca todos os aviões
    tarifas = Tarifa.objects.all()  # Busca todas as tarifas

    if request.method == 'POST':
        form = CobrancaForm(request.POST, instance=cobranca)
        if form.is_valid():
            form.save()
            return redirect('listar_cobrancas')
    else:
        form = CobrancaForm(instance=cobranca)

    return render(request, 'formc.html', {
        'form': form,
        'avioes': avioes,  # Passando aviões para o template
        'tarifas': tarifas  # Passando tarifas para o template
    })


def CobrancaDelete(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        cobranca.delete()
        return redirect('listar_cobrancas')
    return render(request, 'confirmar_exclusão.html', {'cobranca': cobranca})


def CobrancaDetails(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    return render(request, 'detalhes.html', {'cobranca': cobranca})
