from django.shortcuts import render
from . import forms
from django.core.mail import send_mail

# Create your views here.


def registro(request):
    reg = forms.Reservacion()
    if request.method == 'POST':
        reg = forms.Reservacion(request.POST)
        asuntoCliente = "Solicitud recibida en Hostales-Cuba"
        mensajeCliente = "Pronto nos pondremos en contacto con usted."
        para = str(reg['Email'].value())
        send_mail(asuntoCliente,mensajeCliente,'hostales@cd.com',[para])

        return render(request,'reservacion/success.html',{'para':para})

    return render(request,'reservacion/index.html',{'form':reg})