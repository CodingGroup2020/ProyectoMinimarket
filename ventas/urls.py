from django.urls import path
from ventas import views




#aca genero las urls que va a tener la app core de nuestro proyecto 
urlpatterns = [
	path('buscarProducto/',views.BuscarProducto, name="buscarProducto"),
	path('cargaUnaVenta/',views.cargaUnaVenta, name="cargaUnaVenta"),
    path('cargaVenta/',views.cargaVenta, name="cargaVenta"),
    path('muestraVenta/',views.muestraVenta, name="muestraVentas"),
    path('detalle/<int:pk>/',views.cargaDetalle, name="detalle"),
    path('eliminarDetalle/',views.eliminarDetalle, name="eliminarDetalle"),
    path('eliminarVenta/',views.eliminarVenta, name="eliminarVenta"),
	path('actualizarPrecioDetalleVenta/',views.actualizarPrecioCantidadVenta, name="actualizarDetalleVenta"),
	path('terminarVenta/',views.terminarVenta, name="TerminarVenta"),
    

]