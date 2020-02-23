from django.db import models

# Create your models here.
class Producto (models.Model):
    codigo = models.CharField(max_length=100,blank=True,null=True,verbose_name="Codigo de barras")
    nombre = models.CharField(max_length=50,blank=True,null=True,verbose_name="Nombre del producto")
    precioVenta= models.FloatField(blank=True,null=True,verbose_name="Precio de venta del producto")
    precioCompra= models.FloatField(blank=True,null=True,verbose_name="Precio de compra del producto")
    stock= models.IntegerField(blank=True,null=True,verbose_name="Cantidad disponible")
    pesaje= models.FloatField(blank=True,null=True,verbose_name="Pesaje del producto")
    tipoProducto= models.IntegerField()
    def __str__(self):
        return self.codigo
    