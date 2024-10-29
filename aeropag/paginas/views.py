from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    # Se você precisar passar informações personalizadas para o template:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione dados personalizados aqui, se necessário
        return context


# Create your views here.
class IndexView(TemplateView):
    login_url = reverse_lazy('login')
    template_name = "index.html"