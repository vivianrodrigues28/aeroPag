from django.db import models
from django.contrib.auth.models import User
from avioes.models import Aviao

class Cliente(models.Model):
    cli_codigo = models.AutoField(primary_key=True)
    cli_nome = models.CharField(max_length=255)
    cli_email = models.EmailField(max_length=255)
    cli_telefone = models.CharField(max_length=50)
    cli_avi_codigo = models.ForeignKey(Aviao, on_delete=models.CASCADE, related_name='clientes', null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.cli_nome

