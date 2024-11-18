from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ClienteForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from django.http import JsonResponse
from avioes.models import Aviao
def listar_clientes(request):
    # Filtra os clientes do usuário logado
    clientes = Cliente.objects.filter(usuario=request.user)
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def cadastrar_cliente(request):
    avioes = Aviao.objects.all()  # Busca todos os aviões cadastrados
    form = SeuFormularioDeCliente()  # Substitua pelo formulário correto

    if request.method == 'POST':
        form = SeuFormularioDeCliente(request.POST)
        if form.is_valid():
            form.save()
            # Redireciona ou exibe mensagem de sucesso
            return redirect('lista-clientes')

    context = {
        'form': form,
        'avioes': avioes,  # Envia os aviões para o template
    }
    return render(request, 'cadastrar_cliente.html', context)


def excluir_cliente(request, cliente_id):
    if request.method == 'POST':
        try:
            cliente = Cliente.objects.get(pk=cliente_id, usuario=request.user)
            cliente.delete()
            return JsonResponse({'status': 'success'})
        except Cliente.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cliente não encontrado'}, status=404)


def editar_cliente(request, cliente_id):
    if request.method == 'POST':
        try:
            cliente = Cliente.objects.get(pk=cliente_id, usuario=request.user)
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')

            # Atualiza os dados do cliente
            cliente.nome = nome
            cliente.email = email
            cliente.telefone = telefone
            cliente.save()

            return JsonResponse({'status': 'success', 'nome': cliente.nome, 'email': cliente.email, 'telefone': cliente.telefone})
        except Cliente.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cliente não encontrado'}, status=404)


class ClienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    form_class = ClienteForm
    template_name = 'forms.html'
    success_url = reverse_lazy('listar-clientes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o cliente ao usuário atual
        return super().form_valid(form)


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    form_class = ClienteForm
    template_name = 'forms.html'
    success_url = reverse_lazy('listar-clientes')

    def get_object(self, queryset=None):
        return get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)  # Filtra pelo cliente do usuário


class ClienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

    def get_object(self, queryset=None):
        return get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)  # Filtra pelo cliente do usuário


class ClienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'listas/cliente.html'

    def get_queryset(self):
        # Lista apenas os clientes do usuário logado
        return Cliente.objects.filter(id=self.request.user.id)
