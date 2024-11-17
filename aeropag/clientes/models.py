from django.db import models
from django.contrib.auth.models import User
from avioes.models import Aviao

class Cliente(models.Model):
    cli_nome = models.CharField(max_length=255)
    cli_email = models.EmailField()
    cli_telefone = models.CharField(max_length=20)
    # A chave primária 'id' será gerada automaticamente

    def __str__(self):
        return self.cli_nome