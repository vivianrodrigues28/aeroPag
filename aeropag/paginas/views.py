from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from avioes.models import Aviao

def dashboard(request):
    # Conta o total de aviões e obtém a lista completa
    total_avioes = Aviao.objects.count()
    lista_avioes = Aviao.objects.all()

    # Passa essas informações para o template
    context = {
        'total_avioes': total_avioes,
        'lista_avioes': lista_avioes,
    }
    return render(request, 'paginas/dashboard.html', context)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona a lista de aviões ao contexto
        context['lista_avioes'] = Aviao.objects.all()
        context['total_avioes'] = Aviao.objects.count()  # Total de aviões, se necessário
        return context


# Create your views here.
class IndexView(TemplateView):
    login_url = reverse_lazy('login')
    template_name = "index.html"

