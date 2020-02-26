from django.shortcuts import render

# Create your views here.
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from ventas.models import DetalleVenta
from django.template.loader import render_to_string, get_template
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context



def send_email(request):
    #mail=['josecarrenio2@gmail.com']
    idVenta=request.POST.get('idVenta')
    print( idVenta)
    mail=[request.POST.get('mail','')]
    subject='Factura de compra KSI24'
    detalleBody=DetalleVenta.objects.filter(ventas__id=idVenta)
    print(detalleBody)
    total = 0
    for d in detalleBody:
        total+= d.precioProducto

    message = get_template('mails/contenidoMail.html').render({'detalleBody':detalleBody,'total':total})
    if request.method == "POST":
        email=EmailMessage(
            subject,
            message,
            from_email='ksi24larioja@gmail.com',
            to=mail,
            )
        email.content_subtype='html'
        email.send()
    return HttpResponse("Listo, email enviado")