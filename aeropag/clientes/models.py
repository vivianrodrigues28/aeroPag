from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cli_nome = models.CharField(max_length=255)
    cli_email = models.EmailField()
    cli_telefone = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.usuario:
            raise ValueError("O campo 'usuario' é obrigatório em determinados casos.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.cli_nome


