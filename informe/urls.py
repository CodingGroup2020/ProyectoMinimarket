from django.urls import path
from.views import informeTemporal,render1,consultarProductosVendidos
urlpatterns = [
    path('informe2/',informeTemporal,name="informe2"),
    path('informe/',render1,name="informe"),
    path('productosVendidos/',consultarProductosVendidos,name="productosVendidos"),
]
