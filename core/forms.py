from django import forms
from.models import Producto
class formProducto (forms.ModelForm):
    class Meta:
        model=Producto
        fields=[
            'codigo',
            'nombre',
            'precioVenta',
            'precioCompra',
            'stock',
            'pesaje',
            'tipoProducto',
        ]
        labels={
            'codigo':'Codigo de barras',
            'nombre':'Nombre del producto',
            'precioVenta':'Precio de venta del producto',
            'precioCompra':'Precio de compra del producto',
            'stock':'Cantidad de producto',
            'pesaje':'Pesaje del producto',
            'tipoProducto':'tipo de producto',
        }
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control' ,'id':'codigo'}),
            'nombre':forms.TextInput(attrs={'class':'form-control' ,'id':'nombre'}),
            'precioVenta':forms.TextInput(attrs={'class':'form-control' ,'id':'precioVenta'}),
            'precioCompra':forms.TextInput(attrs={'class':'form-control' ,'id':'precioCompra'}),
            'stock':forms.TextInput(attrs={'class':'form-control' ,'id':'stock'}),
            'pesaje':forms.TextInput(attrs={'class':'form-control' ,'id':'pesaje'}),
            'tipoProducto':forms.TextInput(attrs={'class':'form-control' ,'id':'tipoProducto'}),

            
        }
