from django.db import models

class Cliente(models.Model):
    cli_codigo = models.AutoField(primary_key=True)
    cli_nome = models.CharField(max_length=255)
    cli_email = models.EmailField(max_length=255)
    cli_telefone = models.CharField(max_length=50)
    cli_avi_codigo = models.ForeignKey('avioes.Aviao', on_delete=models.CASCADE, related_name='clientes')

    def __str__(self):
        return self.cli_nome
