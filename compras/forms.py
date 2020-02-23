from django import forms
from.models import Compra
class formCompra(forms.ModelForm):
    class Meta:
        model=Compra
        fields=[
            'tipoCompra',
            'fechaCompra',
            'valorCompra',
        ]
        labels={
            'tipoCompra':'Tipo de compra',
            'fechaCompra':'Fecha de compra',
            'valorCompra':'Monto de la compra',
        }
        widgets={
            'tipoCompra':forms.TextInput(attrs={'class':'form-control' ,'id':'tipoCompra'}),
            'fechaCompra':forms.DateInput(attrs={'class':'form-control' ,'id':'fechaCompra'}),
            'valorCompra':forms.TextInput(attrs={'class':'form-control' ,'id':'valorCompra' }),   
        }