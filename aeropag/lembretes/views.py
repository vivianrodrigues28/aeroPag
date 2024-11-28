from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Lembrete
from .forms import LembreteForm  

def editar_lembrete(request, lembrete_id):
    lembrete = get_object_or_404(Lembrete, pk=lembrete_id)
    if request.method == 'POST':
        form = LembreteForm(request.POST, instance=lembrete)
        if form.is_valid():
            form.save()
            return redirect('listar-lembretes')
    else:
        form = LembreteForm(instance=lembrete)

    return render(request, 'editar_lembrete.html', {'form': form, 'lembrete': lembrete})


def excluir_lembrete(request, pk):
    lembrete = get_object_or_404(Lembrete, pk=pk)
    if request.method == 'POST':
        lembrete.delete()
        return redirect('listar-lembretes') 


# View para cadastrar lembrete
def cadastrar_lembrete(request):
    if request.method == "POST":
        form = LembreteForm(request.POST)
        if form.is_valid():
            lembrete = form.save(commit=False)
            lembrete.usuario = request.user 
            lembrete.save()
            return redirect('listar-lembretes')  # Redireciona para a página de lista de lembretes
    else:
        form = LembreteForm()

    return render(request, 'cadastro_lembrete.html', {'form': form})

# View para excluir lembrete
def excluir_lembrete(request, id):
    lembrete = get_object_or_404(Lembrete, pk=id)  # Obtém o lembrete pelo ID
    lembrete.delete()  # Exclui o lembrete
    return redirect('listar-lembretes')  # Redireciona para a lista de lembretes

# View para criar lembrete utilizando a classe CreateView
class LembreteCreate(LoginRequiredMixin, CreateView):
    model = Lembrete
    fields = ['titulo', 'descricao', 'obs', 'relevancia', 'data']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-lembretes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associando o lembrete ao usuário logado
        return super().form_valid(form)

# View para editar lembrete utilizando a classe UpdateView
class LembreteUpdate(LoginRequiredMixin, UpdateView):
    model = Lembrete
    fields = ['titulo', 'descricao', 'obs', 'relevancia', 'data']
    template_name = 'editar_lembrete.html'
    success_url = reverse_lazy('listar-lembretes')

    def get_object(self):
        return get_object_or_404(Lembrete, pk=self.kwargs['pk'], usuario=self.request.user)

# View para excluir lembrete utilizando a classe DeleteView
class LembreteDelete(LoginRequiredMixin, DeleteView):
    model = Lembrete
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-lembretes')

    def get_object(self):
        return get_object_or_404(Lembrete, pk=self.kwargs['pk'], usuario=self.request.user)

# View para listar os lembretes
class LembreteList(LoginRequiredMixin, ListView):
    model = Lembrete
    template_name = 'listas/lembrete.html'

    def get_queryset(self):
        return Lembrete.objects.filter(usuario=self.request.user)  # Filtrando pelos lembretes do usuário logado
