from django.urls import path
from.views import cargaProd,home,actualizaProducto,borrarProducto
urlpatterns = [
    path('',home,name="home"),
    path('cargaproducto/',cargaProd,name="cargaproducto"),
    path('editaProducto/<int:pk>/',actualizaProducto.as_view(),name="editaProducto"),
    path('borraProducto/<int:pk>/',borrarProducto.as_view(),name="borraProducto"),
]
