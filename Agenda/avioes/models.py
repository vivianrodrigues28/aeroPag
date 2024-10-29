from django.db import models

class Aviao(models.Model):
    avi_codigo = models.AutoField(primary_key=True)
    avi_prefixo_do_aviao = models.CharField(max_length=50)
    avi_toneladas = models.DecimalField(max_digits=10, decimal_places=2)
    avi_grupo = models.IntegerField()

    def __str__(self):
        return self.avi_prefixo_do_aviao
