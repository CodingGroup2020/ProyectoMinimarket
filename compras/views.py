from django.shortcuts import render,reverse
from.models import Compra
from.forms import formCompra
from django.views.generic import UpdateView,DeleteView
# Create your views here.
def cargaCompra(request):
    compras=Compra.objects.all()
    if request.method=='POST':
        form=formCompra(request.POST)
        if form.is_valid():
            form.save()
        return render (request,'compras/cargaCompra.html',{'form':form,'compras':compras})
    else:
        form=formCompra()
        return render (request,'compras/cargaCompra.html',{'form':form,'compras':compras})
class borrarCompra(DeleteView):
    model=Compra
    template_name='compras/borraCompra.html'
    def get_success_url(self):
        return reverse ('cargaCompra')
class edicaCompra(UpdateView):
    model=Compra
    form_class=formCompra
    template_name='compras/editaCompra.html'
    def get_success_url(self):
        return reverse ('cargaCompra')
