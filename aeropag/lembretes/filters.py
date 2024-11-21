import django_filters
from .models import Lembrete
from datetime import date, timedelta

class LembreteFilter(django_filters.FilterSet):
    filtro_data = django_filters.CharFilter(method='filter_by_date', label='Filtro por data')

    class Meta:
        model = Lembrete
        fields = [] 
    def filter_by_date(self, queryset, name, value):
        hoje = date.today()

        if value == 'hoje':
            return queryset.filter(data=hoje)
        elif value == 'prox_semana':
            semana_fim = hoje + timedelta(days=7)
            return queryset.filter(data__range=[hoje, semana_fim])
        elif value == 'ante_semana':
            semana_inicio = hoje - timedelta(days=7)
            return queryset.filter(data__range=[semana_inicio, hoje])
        elif value == 'ante_tudo':
            return queryset.filter(data__lt=hoje)
        elif value == 'prox_mes':
            mes_fim = hoje.replace(day=28) + timedelta(days=4)  # Final do mês atual
            return queryset.filter(data__month=hoje.month)
        elif value == 'tudo':
            return queryset.all()
        else:
            return queryset
