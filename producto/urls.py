from django.urls import path
from.views import busquedaycarga
urlpatterns = [
    path ('cargaproducto/',busquedaycarga, name='producto'),
]
