from django.db import models

# Create your models here.
class GastosFijos(models.Model):
    tipoGastos=models.CharField(max_length=100,verbose_name="Tipo de gasto",null=True,blank=True)
    detalle=models.TextField(blank=True,null=True,verbose_name="Detalle del pago")
    fechaPago=models.DateField(blank=True,null=True,verbose_name="Fecha de pago")
    valor=models.IntegerField(blank=True,null=True,verbose_name="Monto del pago")
    def __str__(self):
        return self.tipoGastos
    