from django.db import models
from django.contrib.auth.models import User


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
    cob_codigo = models.CharField(max_length=20)
    tar_codigo = models.CharField(max_length=20)
    quantidade_horas = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    avi_codigo = models.CharField(max_length=20)

    def calcular_valor(self):
        if self.tar.tipo_voo == 'domestico':
            return self.quantidade_horas * self.tar.valor_domestico
        else:
            return self.quantidade_horas * self.tar.valor_internacional

    def save(self, *args, **kwargs):
        try:
        # Obter a instância de Tarifa e Aviao a partir dos códigos
            self.tar = Tarifa.objects.get(tar_codigo=self.tar_codigo)
            self.avi = Aviao.objects.get(avi_codigo=self.avi_codigo)

        # Verificar se a tonelagem do avião está dentro dos limites da tarifa
            if not (self.tar.tar_ton_min <= self.avi.avi_toneladas <= self.tar.tar_ton_max):
                raise ValueError('A tonelagem do avião está fora dos limites permitidos para esta tarifa.')

        # Calcular o valor total da cobrança
            self.valor_total = self.calcular_valor()

        # Chamar o método save do modelo para salvar os dados
            super().save(*args, **kwargs)

        except ObjectDoesNotExist as e:
            raise ValueError(f'Erro ao encontrar o objeto: {e}')

# Create your models here.
