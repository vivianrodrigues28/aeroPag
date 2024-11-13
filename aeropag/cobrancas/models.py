from django.db import models

class Aviao(models.Model):
    avi_codigo = models.AutoField(primary_key=True)
    avi_prefixo_do_aviao = models.CharField(max_length=50)
    avi_toneladas = models.DecimalField(max_digits=10, decimal_places=2)
    avi_grupo = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
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
        # Verificar se a tonelagem está dentro dos limites da tarifa
        if not (self.tar.ton_min <= self.avi.tonelada<= self.tar.ton_max):
            raise ValueError('A tonelagem do avião está fora dos limites permitidos para esta tarifa.')

        # Calcular o valor total com base no tipo de voo e horas
        self.valor_total = self.calcular_valor()
        super().save(*args, **kwargs)

# Create your models here.
