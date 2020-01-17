from django.db import models

# Create your models here.
class Producto (models.Model):
    codigo_prod=models.CharField(max_length=50,primary_key=True,verbose_name="Codigo de barra del producto")
    descripcio=models.CharField(max_length=100,verbose_name="Descripcion del producto")
    precio=models.FloatField(null=True, blank=True)
    cantidad =models.IntegerField(blank=True , null=True)
    def __str__(self):
        return self.descripcio
    