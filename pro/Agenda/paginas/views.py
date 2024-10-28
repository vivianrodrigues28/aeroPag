from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

# Create your views here.
class IndexView(TemplateView):
    login_url = reverse_lazy('login')
    template_name = "index.html"