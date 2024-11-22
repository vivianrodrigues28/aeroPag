from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from tarifas.models import Tarifa

class Aviao(models.Model):
    avi_codigo = models.AutoField(primary_key=True)
    avi_prefixo_do_aviao = models.CharField(max_length=50)
    avi_toneladas = models.DecimalField(max_digits=10, decimal_places=2)
    avi_grupo = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cobrancas_usuario')
    
    def __str__(self):
        return self.avi_prefixo_do_aviao

class Tarifa(models.Model):
    
    tar_codigo = models.AutoField(primary_key=True)
    tar_tipo = models.CharField(max_length=255)
    tar_valor_domestico = models.DecimalField(max_digits=10, decimal_places=2)
    tar_valor_internacional = models.DecimalField(max_digits=10, decimal_places=2)
    tar_grupo = models.IntegerField()
    tar_ton_min = models.IntegerField()
    tar_ton_max = models.IntegerField()


    def __str__(self):
        return self.tar_tipo




class Cobranca(models.Model):
    cob_codigo = models.CharField(max_length=10)
    avi_codigo = models.CharField(max_length=10)
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




