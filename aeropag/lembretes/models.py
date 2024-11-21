from django.db import models
from django.contrib.auth.models import User

class Lembrete(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Título")
    descricao = models.CharField(max_length=250, blank=True, default='', verbose_name="Descrição")
    obs = models.CharField(max_length=50, blank=True, default='', verbose_name="OBS")
    relevancia = models.IntegerField(default=1, verbose_name="Grau de Relevância")
    data = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-relevancia'] 
    def __str__(self):
        return "{} ({}) - {}".format(self.titulo, self.obs, self.data)

    def is_past_due(self):
        return self.data < date.today()

