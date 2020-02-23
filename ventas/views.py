from django.shortcuts import render,reverse,HttpResponse
from .models import Venta,DetalleVenta,Producto
from.forms import formVenta,formDetalle
import json
from datetime import date
from datetime import datetime
from django.http import JsonResponse
# Create your views here.

def cargaUnaVenta(request):
  print(request.POST)
  if request.method == 'POST':
    form=formVenta(request.POST)
    if form.is_valid():
      form.save()
      ultimoIdVenta=Venta.objects.last()
      today = date.today()
      fecha= str(today)
      idVentaUltimo= str(ultimoIdVenta)
    # return HttpResponse(ultimoIdVenta)
    # return JsonResponse({'ultimoIdVenta':ultimoIdVenta,'fechaActual':today})
      response_data = {}
      response_data['idVentaUltimo'] = idVentaUltimo
      response_data['fecha'] = fecha
    return HttpResponse(json.dumps(response_data), content_type="application/json")
  else:
    return HttpResponse("error")


def cargaVenta(request):
  form=formVenta(request.POST)
  form2 = formDetalle(request.POST)
  today = date.today()
  print(today)
  return render(request,"ventas/cargaventa.html",{'form':form,'formDetalle':form2,'fecha':today})


def muestraVenta(request):
  ventas=Venta.objects.all()
  return render(request,"ventas/muestraventa.html",{'ventas':ventas})


def BuscarProducto(request):
  if request.method=='POST':
    productos=Producto.objects.filter(codigo__icontains=request.POST['codigoProducto'] ).values('id','codigo','nombre','precioVenta','stock','tipoProducto')
    return HttpResponse( json.dumps( list(productos)), content_type='application/json' )  
  else:
      return HttpResponse("errorrr")

def cargaDetalle(request,pk): 
  productos=DetalleVenta.objects.filter(ventas__id=pk).values('id')
  # print(request.POST['precioProducto'])
  if request.method=='POST':
        form = formDetalle(request.POST)
        if form.is_valid():
            form.save()
        # return HttpResponse(productos)
            idDetalleVenta= DetalleVenta.objects.last()
        return HttpResponse( idDetalleVenta)    
      
  else:
 
      return HttpResponse("errorrr")


def eliminarDetalle(request):
    pk = request.POST.get('idDetalleVenta')
    print(pk)
    identificador = DetalleVenta.objects.get(pk=pk)
    identificador.delete()
    # response = {}
    # return JsonResponse(response)s
    return HttpResponse("lsito broly")



def eliminarVenta(request):
    pk = request.POST.get('idVenta')
    print(pk)
    identificador = Venta.objects.get(pk=pk)
    identificador.delete()
    # response = {}
    # return JsonResponse(response)s
    return HttpResponse("Eliminado")

def actualizarPrecioCantidadVenta(request):
    pk = request.POST.get('idDetalleVenta')
    precio = request.POST.get('precioDetalleVenta')
    print(pk)
    print(precio)
    identificador = DetalleVenta.objects.filter(pk=pk)
    identificador.update(precioProducto=precio)
    return HttpResponse("Actualizado")


def terminarVenta(request):
    pk = request.POST.get('idVenta')
    precioTotal = request.POST.get('precioVentaTotal')
    identificador = Venta.objects.filter(pk=pk)
    identificador.update(totalVenta=precioTotal)
    return HttpResponse("Venta Terminada")

