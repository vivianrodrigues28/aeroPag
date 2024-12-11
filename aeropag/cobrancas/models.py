from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from tarifas.models import Tarifa
from avioes.models import Aviao
from decimal import Decimal

class Cobranca(models.Model):
    cob_codigo = models.CharField(max_length=10)
    avi_codigo = models.ForeignKey(Aviao, on_delete=models.CASCADE, related_name='cobrancas')
    tar_codigo = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    quantidade_horas = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Cobrança {self.cob_codigo}"

    def save(self, *args, **kwargs):
        # Obtenção de informações do avião e tarifa
        aviao = self.avi_codigo
        tarifa = self.tar_codigo

        # Identificação do tipo de voo (doméstico/internacional)
        tipo_voo = "doméstico" if aviao.tipo_voo == "D" else "internacional"

        # Tarifa base (com ATAERO aplicado)
        if tipo_voo == "doméstico":
            tarifa_base = tarifa.tar_valor_domestico
        else:
            tarifa_base = tarifa.tar_valor_internacional
        
        tarifa_base_com_ataero = tarifa_base * Decimal(1.359)

        # Calculando valores de acordo com o grupo tarifário
        if tarifa.tar_grupo == 1:  # Pouso
            self.valor_total = tarifa_base_com_ataero
        elif tarifa.tar_grupo == 2:  # Permanência
            horas_cobradas = max(self.quantidade_horas - 3, 0)  # Desconsiderar as 3 primeiras horas
            self.valor_total = tarifa_base_com_ataero * horas_cobradas
        elif tarifa.tar_grupo == 3:  # Estadia
            self.valor_total = tarifa_base_com_ataero * self.quantidade_horas
        elif tarifa.tar_grupo == 4:  # Comunicação e Navegação Aérea (TAN e TAT)
            self.valor_total = tarifa_base_com_ataero

        # Salvar o modelo
        super().save(*args, **kwargs)



