from django.db import models

# Create your models here.
class Compra(models.Model):
    tipoCompra=models.CharField(max_length=100,verbose_name="Tipo de Compra",blank=True,null=True)
    fechaCompra=models.DateField(null=True,blank=True,verbose_name="Fecha de la compra")
    valorCompra=models.IntegerField(verbose_name="Monto de la compra",blank=True,null=True)
    def __str__(self):
        return self.tipoCompra
    