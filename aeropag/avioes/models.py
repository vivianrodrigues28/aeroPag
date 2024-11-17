from django.db import models
from django.contrib.auth.models import User

class Aviao(models.Model):
    avi_codigo = models.AutoField(primary_key=True)
    avi_prefixo_do_aviao = models.CharField(max_length=10) 
    avi_toneladas = models.DecimalField(max_digits=10, decimal_places=2)
    avi_grupo = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    
    def __str__(self):
        return self.avi_prefixo_do_aviao
