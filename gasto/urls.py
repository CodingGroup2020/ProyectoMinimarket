from django.urls import path
from.views import cargaGasto,editaGasto,borraGasto
urlpatterns = [
    path('cargagasto/',cargaGasto,name="gasto"),
    path('editaGasto/<int:pk>/',editaGasto.as_view(),name="editaGasto"),
    path('borraGasto/<int:pk>/',borraGasto.as_view(),name="borraGasto"),
]

