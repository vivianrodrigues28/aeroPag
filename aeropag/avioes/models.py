from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente  

class Aviao(models.Model):
    avi_codigo = models.AutoField(primary_key=True)
    avi_prefixo_do_aviao = models.CharField(max_length=10) 
    avi_toneladas = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='avioes_usuario')
    cli_nome = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='avioes_cliente',  null=True, blank=True)  
    
    
    
    def __str__(self):
        return f"{self.avi_prefixo_do_aviao} - {self.cliente.cli_nome}" 
