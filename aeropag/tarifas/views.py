from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Tarifa
from .forms import TarifaForm
from django.http import JsonResponse
from django.contrib import messages


def listar_tarifas(request):
    
    tarifas = Tarifa.objects.filter(usuario=request.user)
    return render(request, 'lista_tarifas.html', {'tarifas': tarifas})


def criar_tarifa(request):
    if request.method == 'POST':
        form = TarifaForm(request.POST)
        if form.is_valid():
            tarifa = form.save(commit=False)
            tarifa.usuario = request.user
            tarifa.save()
            return redirect('listar-tarifas')  
    else:
        form = TarifaForm()
    return render(request, 'cadastrar_tarifa.html', {'form': form})

def editar_tarifa(request, tarifa_id):
    tarifa = get_object_or_404(Tarifa, pk=tarifa_id, usuario=request.user)
    if request.method == 'POST':
        form = TarifaForm(request.POST, instance=tarifa)
        if form.is_valid():
            form.save()
            return redirect('listar-tarifas')  
    else:
        form = TarifaForm(instance=tarifa)
    return render(request, 'editar_tarifa.html', {'form': form})


def excluir_tarifa(request, tarifa_id):
    if request.method == 'POST':
        try:
            tarifa = Tarifa.objects.get(pk=tarifa_id, usuario=request.user)
            tarifa.delete()
            return JsonResponse({'status': 'success'})
        except Tarifa.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Tarifa não encontrada'}, status=404)





class TarifaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm
    template_name = 'formas.html'
    success_url = reverse_lazy('listar-tarifas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Tarifa criada com sucesso!")
        return super().form_valid(form)

class TarifaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm
    template_name = 'formas.html'
    success_url = reverse_lazy('listar-tarifas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "Tarifa atualizada com sucesso!")
        return super().form_valid(form)


class TarifaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tarifa
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-tarifas')

    def get_object(self, queryset=None):
        return get_object_or_404(Tarifa, pk=self.kwargs['pk'], usuario=self.request.user)  

class TarifaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tarifa
    template_name = 'listas/tarifa.html'

    def get_queryset(self):
        
        return Tarifa.objects.filter(usuario=self.request.user)

