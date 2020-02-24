from django.urls import path
from.views import informeTemporal,render1,consultarProductosVendidos,balance,balance2
urlpatterns = [
    path('informe2/',informeTemporal,name="informe2"),
    path('informe/',render1,name="informe"),
    path('productosVendidos/',consultarProductosVendidos,name="productosVendidos"),
    path('balance2/',balance2,name="balance2"),
    path('balance/',balance,name="balance"),
]
