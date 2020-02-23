from django import forms
from.models import Venta,DetalleVenta
class formVenta(forms.ModelForm):
    class Meta:
        model=Venta
        fields = [
            'usuario',
        ]
class formDetalle(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=[
            'ventas',
            'producto',
            'precioProducto',
        ]