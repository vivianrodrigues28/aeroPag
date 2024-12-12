from django.db import models
from tarifas.models import Tarifa
from avioes.models import Aviao

class Cobranca(models.Model):
    cob_codigo = models.CharField(max_length=10)
    avi_codigo = models.ForeignKey(Aviao, on_delete=models.CASCADE, related_name='cobrancas')
    tar_codigo = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    quantidade_horas = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   
    def __str__(self):
        return f"Cobrança {self.cob_codigo}"

    def save(self, *args, **kwargs):
        # Busca o avião e tarifa associada
        aviao = self.avi_codigo
        tarifa = self.tar_codigo

        # Verifica o tipo de voo (doméstico ou internacional)
        if tarifa.tar_tipo == 'doméstico':
            valor_tarifa = tarifa.tar_valor_domestico
        else:
            valor_tarifa = tarifa.tar_valor_internacional

        # Verifica se a tonelagem do avião está dentro dos limites da tarifa
        if aviao.avi_toneladas < tarifa.tar_ton_min or aviao.avi_toneladas > tarifa.tar_ton_max:
            raise ValueError('A tonelagem do avião não está dentro dos limites da tarifa.')

        # Calcula o valor total com base nas horas de voo e na tarifa
        self.valor_total = self.quantidade_horas * valor_tarifa
        super().save(*args, **kwargs)
