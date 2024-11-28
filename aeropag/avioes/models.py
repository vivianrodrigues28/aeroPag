from django.db import models
from django.contrib.auth.models import User

# models.py

class Aviao(models.Model):
    avi_prefixo_do_aviao = models.CharField(max_length=10)
    avi_grupo = models.IntegerField()
    avi_toneladas = models.FloatField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.avi_prefixo_do_aviao

class Cobranca(models.Model):
    aviao = models.ForeignKey(Aviao, on_delete=models.CASCADE)  # Referência ao modelo Aviao
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cobrança {self.id} - {self.aviao.avi_prefixo_do_aviao}"

