from django.shortcuts import render,redirect,reverse

# Create your views here.
from.models import Producto #se importa el modelo para traerlo y listarlo
from.forms import formProducto # se importa el formulario para hacer efectiva la carga 
from django.views.generic import UpdateView,DeleteView
def home(request):
    return render(request,'core/home.html')

# funcion de carga y listado del formulario.

def cargaProd(request):
    productos=Producto.objects.all# aca estoy trayendo el modelo Producto para que se pueda renderizar en el html en la tabla
    if request.method=='POST':
        form = formProducto(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'core/cargaproducto.html',{'form':form,'productos':productos}) #si se guarda como corresponde se carga la misma pagina 
    else:
        form=formProducto
        return render(request,'core/cargaproducto.html',{'form':form,'productos':productos})
class actualizaProducto(UpdateView):
    model=Producto
    form_class=formProducto
    template_name='core/editaproducto.html'
    def get_success_url(self):
        return reverse('cargaproducto')#si se edita correctamente vuelve a la pagina principal de los productos
class borrarProducto(DeleteView):
    model=Producto
    template_name='core/borraproducto.html'
    def get_success_url(self):
        return reverse('cargaproducto')#si se edita correctamente vuelve a la pagina principal de los productos


