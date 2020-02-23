from django import forms
from.models import GastosFijos

class formGastos(forms.ModelForm):
    class Meta:
        model=GastosFijos
        fields=[
            'tipoGastos',
            'detalle',
            'fechaPago',
            'valor',
        ]
        labels={
            'tipoGastos':'Tipo de gasto',
            'detalle':'Detalle de gasto',
            'fechaPago':'Fecha del pago',
            'valor':'Monto del pago',
        }
        widgets={
            'tipoGastos':forms.TextInput(attrs={'class':'form-control' ,'id':'tipoGastos' }),
            'detalle':forms.TextInput(attrs={'class':'form-control' ,'id':'detalle'}),
            'fechaPago':forms.DateInput(attrs={'class':'form-control' ,'id':'fechaPago'}),  
            'valor':forms.TextInput(attrs={'class':'form-control' ,'id':'valor'}),
        }