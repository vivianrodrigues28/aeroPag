from django.core.exceptions import ValidationError
from django.db import models

class Tarifa(models.Model):
    tar_codigo = models.AutoField(primary_key=True)
    tar_tipo = models.CharField(max_length=255)
    tar_valor_domestico = models.DecimalField(max_digits=10, decimal_places=2)
    tar_valor_internacional = models.DecimalField(max_digits=10, decimal_places=2)
    tar_grupo = models.IntegerField()
    tar_ton_min = models.IntegerField()
    tar_ton_max = models.IntegerField()

    def clean(self):
        # Validação personalizada
        if self.tar_ton_min > self.tar_ton_max:
            raise ValidationError('O valor mínimo de tonelagem não pode ser maior que o valor máximo.')
        if self.tar_ton_max < self.tar_ton_min:
            raise ValidationError('O valor máximo de tonelagem não pode ser menor que o valor mínimo.')

    def __str__(self):
        return self.tar_tipo
