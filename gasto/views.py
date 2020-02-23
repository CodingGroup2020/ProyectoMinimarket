from django.shortcuts import render,reverse,redirect
from.forms import formGastos
from.models import GastosFijos
from django.views.generic import UpdateView,DeleteView
# Create your views here.
def cargaGasto(request):
    gastos=GastosFijos.objects.all()
    if request.method=='POST':
        form=formGastos(request.POST)
        if form.is_valid():
            form.save()
        return render,(request,'gasto/cargagasto.html',{'form':form,'gastos':gastos}) 
    else:
        form=formGastos
        return render(request,'gasto/cargagasto.html',{'form':form,'gastos':gastos})
class editaGasto(UpdateView):
    model=GastosFijos
    form_class=formGastos
    template_name='gasto/editagasto.html'
    def get_success_url(self):
        return reverse ('gasto')
class borraGasto(DeleteView):
    model=GastosFijos
    template_name='gasto/borragasto.html'
    def get_success_url(self):
        return reverse ('gasto')
