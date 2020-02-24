from django.shortcuts import render,HttpResponse
from datetime import datetime
from ventas.models import Venta
from ventas.models import DetalleVenta,Producto
import json
from django.core.serializers import serialize
from ventas.models import Venta,DetalleVenta    
from core.models import Producto
from gasto.models import GastosFijos
from compras.models import Compra


# Create your views here.
def informeTemporal(request):
    fechaIninicial=request.POST.get('fechaUno')
    fechaLimite=request.POST.get('fechaDos')
    usuario = request.POST.get('usuario')
    fechaI= datetime.strptime(fechaIninicial, "%Y-%m-%d")
    fechaL= datetime.strptime(fechaLimite, "%Y-%m-%d")
    #fechaI=datetime.strptime(fechaIninicial, '%Y/%dd/%mm').date()
    #fechaL=datetime.strptime(fechaLimite, '%Y/%dd/%mm').date()
    print (fechaI ,"ESTAS SON LAS FECHAS EN DATE", fechaL , "user : ", usuario)
    fechaDetalle=serialize('json', Venta.objects.filter(usuario=usuario).filter(fecha__range=(fechaI,fechaL)))
    #print(fechaDetalle)
    strcut=json.loads(fechaDetalle)
    data=json.dumps(strcut)
    return HttpResponse( data,content_type='application/json' )



def render1(request):
    return render(request,'informe/informe.html')


def consultarProductosVendidos(request):
    idVenta = request.POST.get('idVenta')
    # selecciono modelo del cual queremos traer los campos, y especificamos la tabla relacionada y el campo con la llave foranea
    productosVendidos=serialize('json',Producto.objects.filter(detalleventa__ventas_id=idVenta))
    precioProductosVendidos=serialize('json',DetalleVenta.objects.filter(ventas=idVenta))
    #print(precioProductosVendidos)
    strcut=json.loads(productosVendidos)
    strcut2=json.loads(precioProductosVendidos)
    data=json.dumps(strcut+strcut2)
    return HttpResponse( data, content_type='application/json' )  


def balance(request):
    fechaIninicial=request.POST.get('fechaUno')
    fechaLimite=request.POST.get('fechaDos')
    fechaI= datetime.strptime(fechaIninicial, "%Y-%m-%d")
    fechaL= datetime.strptime(fechaLimite, "%Y-%m-%d")
    fechaBalanceVenta=serialize('json', Venta.objects.filter(fecha__range=(fechaI,fechaL)))
    fechaBalanceCompra=serialize('json', Compra.objects.filter(fechaCompra__range=(fechaI,fechaL)))
    fechaBalanceGasto=serialize('json', GastosFijos.objects.filter(fechaPago__range=(fechaI,fechaL)))
    #print(fechaBalanceVenta)
    strcut=json.loads(fechaBalanceVenta)
    strcut2=json.loads(fechaBalanceCompra)
    strcut3=json.loads(fechaBalanceGasto)
    data=json.dumps(strcut+strcut2+strcut3)
    return HttpResponse( data,content_type='application/json' )

def balance2(request):
    return render(request,'informe/balance.html')