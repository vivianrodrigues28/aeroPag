# paginas/models.py
from django.db import models

class Aviao(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    # Outros campos, se necessário
