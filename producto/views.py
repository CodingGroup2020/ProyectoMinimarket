from django.shortcuts import render,redirect
from.models import Producto
from.forms import productoForm
# Create your views here.
def busquedaycarga(request):
    productos=Producto.objects.all
    #return render (request,'producto/nuevo_producto.html',{})
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            form.save()
        return render (request,'producto/nuevo_producto.html',{'form':form,'productos':productos})
    else:
        form=productoForm()
        return render (request,'producto/nuevo_producto.html',{'form':form,'productos':productos})