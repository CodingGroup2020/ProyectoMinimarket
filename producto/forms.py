from django.forms import ModelForm
from.models import Producto
class productoForm (ModelForm):
    class Meta:
        model=Producto
        fields=[

            'codigo_prod',
            'descripcio',
            'precio',
            'cantidad',
        ]
        labels={
            'codigo_prod':'Codigo de barra del producto',
            'descripcio':'Descripcion del producto',
            'precio':'Precio',
            'cantidad':'Cantidad del producto',

        }