from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from tarifas.models import Tarifa
from avioes.models import Aviao



class Cobranca(models.Model):
    cob_codigo = models.CharField(max_length=10)
    avi_codigo = models.ForeignKey(Aviao, on_delete=models.CASCADE, related_name='cobrancas')
    tar_codigo = models.ForeignKey(Tarifa, on_delete=models.CASCADE )
    quantidade_horas = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Cobrança {self.cob_codigo}"
    

    def save(self, *args, **kwargs):
    #cálculo do valor total com base em tarifa e horas
        tarifa = 100  # Substitua pelo valor correto ou busque da tabela de tarifas
        self.valor_total = self.quantidade_horas * tarifa
        super().save(*args, **kwargs)




