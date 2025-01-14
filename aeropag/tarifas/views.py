from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Tarifa
from .forms import TarifaForm
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render

def editar_tarifa(request, pk):
    tarifa = get_object_or_404(Tarifa, pk=pk)
    if request.method == 'POST':
        form = TarifaForm(request.POST, instance=tarifa)
        if form.is_valid():
            form.save()
            return redirect('listar-tarifas')  # Redireciona para a lista de tarifas após salvar
    else:
        form = TarifaForm(instance=tarifa)
    return render(request, 'editar_tarifa.html', {'form': form})
class TarifaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tarifa
    form_class = TarifaForm
    template_name = 'formas.html'
    success_url = reverse_lazy('listar-tarifas')

    def form_valid(self, form):
        print("Form is valid!")
        form.instance.usuario = self.request.user
        messages.success(self.request, "Tarifa criada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid:", form.errors)
        return super().form_invalid(form)

  

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
        
def listar_tarifas(request):
    tarifas = Tarifa.objects.all()
    return render(request, 'listas/tarifa.html', {'object_list': tarifas})
