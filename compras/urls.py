from django.urls import path
from.views import cargaCompra,edicaCompra,borrarCompra
urlpatterns = [
    path('cargaCompra/',cargaCompra,name="cargaCompra"),
    path('editaCompra/<int:pk>/',edicaCompra.as_view(),name="editaCompra"),
    path('borraCompra/<int:pk>/',borrarCompra.as_view(),name="borraCompra"),
]
