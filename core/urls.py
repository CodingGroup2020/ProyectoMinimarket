from django.urls import path
from django.contrib.auth.views import LoginView 
from django.contrib.auth import views as auth_views
from.views import cargaProd,home,actualizaProducto,borrarProducto,logout
urlpatterns = [
    path('principal/',home,name="home"),
    path('cargaproducto/',cargaProd,name="cargaproducto"),
    path('editaProducto/<int:pk>/',actualizaProducto.as_view(),name="editaProducto"),
    path('borraProducto/<int:pk>/',borrarProducto.as_view(),name="borraProducto"),
    path ('logout/',logout,name='salir'),
    path('', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),

    

]
