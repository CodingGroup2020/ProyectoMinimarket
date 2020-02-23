
from django.db import models
from core.models import Producto
# Create your models here.
class Venta (models.Model):
    fecha = models.DateField(auto_now=True)
    usuario= models.CharField(max_length=30,blank=True,null=True)
    totalVenta = models.FloatField(blank=True,null=True)
    def __str__(self):
        return '%s' % (self.id)


    	
class DetalleVenta(models.Model):
    ventas=models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    precioProducto=models.FloatField(blank=True,null=True) #precio variable de acuerdo a lacantidad del producto es fracionado
    def __str__(self):
        return '%s' % (self.id)

    
    