from django.db import models
from django.contrib.auth.models import User

class Aviao(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    
class Lembrete(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()  
    
    
    

    def __str__(self):
        return f"{self.nome} - {self.data}"



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome

class Tarifa(models.Model):
    PREFERENCIA_CHOICES = [
        ('PATIO', 'Pátio'),
        ('HANGAR', 'Hangar'),
    ]
    
    GRUPO_CHOICES = [
        ('I', 'Grupo I'),
        ('II', 'Grupo II'),
    ]
    
    tipo_preferencia = models.CharField(max_length=10, choices=PREFERENCIA_CHOICES)
    valor_domestico = models.DecimalField(max_digits=10, decimal_places=2)
    valor_internacional = models.DecimalField(max_digits=10, decimal_places=2)
    grupo = models.CharField(max_length=10, choices=GRUPO_CHOICES)
    tonelada_maxima = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Tarifa {self.grupo} - {self.tipo_preferencia}"



class Atividade(models.Model):
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField()

    def __str__(self):
        return self.descricao

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateTimeField()

    def __str__(self):
        return self.nome


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.user.username