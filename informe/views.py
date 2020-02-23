from django.shortcuts import render,HttpResponse
from datetime import datetime
from ventas.models import Venta
from ventas.models import DetalleVenta,Producto
import json
from django.core.serializers import serialize


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
    print(fechaDetalle)
    strcut=json.loads(fechaDetalle)
    data=json.dumps(strcut)
    return HttpResponse( data,content_type='application/json' )



def render1(request):
    return render(request,'informe/informe.html')



def consultarProductosVendidos(request):
    idVenta = request.POST.get('idVenta')

    # selecciono modelo del cual queremos traer los campos, y especificamos la tabla relacionada y el campo con la llave foranea
    productosVendidos=Producto.objects.filter(detalleventa__ventas_id=idVenta).values('nombre')
    return HttpResponse( json.dumps( list(productosVendidos)), content_type='application/json' )  

