from django.shortcuts import render, get_object_or_404, redirect
from .models import Cobranca
from .forms import CobrancaForm
from django.shortcuts import render
 

def criar_cobranca(request):
    if request.method == 'POST':
        form = CobrancaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_cobrancas') 
    else:
        form = CobrancaForm()
    
    return render(request, 'formc.html', {'form': form})
def CobrancaList(request):
    cobrancas = Cobranca.objects.all()
    return render(request, 'cobranca_list.html', {'object_list': cobrancas})


def detalhes_cobranca(request, cobranca_id):
    cobranca = Cobranca.objects.get(id=cobranca_id)
    return render(request, 'detalhes_cobranca.html', {'cobranca': cobranca})

def listar_cobrancas(request):
    
    return render(request, 'listar_cobrancas.html')


def CobrancaCreate(request):
    if request.method == 'POST':
        form = CobrancaForm(request.POST)
        if form.is_valid():
            try:
                cobranca = form.save(commit=False)
                cobranca.save()
                return redirect('listar_cobrancas')
            except Exception as e:
                form.add_error(None, f"Erro ao salvar a cobrança: {str(e)}")
    else:
        form = CobrancaForm()
    return render(request, 'formc.html', {'form': form})


def CobrancaUpdate(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        form = CobrancaForm(request.POST, instance=cobranca)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_cobrancas')
            except Exception as e:
                form.add_error(None, f"Erro ao atualizar a cobrança: {str(e)}")
    else:
        form = CobrancaForm(instance=cobranca)
    return render(request, 'templates/formc.html', {'form': form})


def CobrancaDelete(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        cobranca.delete()
        return redirect('listar_cobrancas')
    return render(request, 'templates/confirmar_exclusão.html', {'cobranca': cobranca})

def CobrancaDetails(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    return render(request, 'detalhes.html', {'cobranca': cobranca})
