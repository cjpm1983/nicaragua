from django.shortcuts import render
from django.core.mail import send_mail
from reservacion import forms

from hostal.models import Hostal

def HostalDetallesView(request, hostal_id):

    reg = forms.Reservacion()

    hosta = Hostal.objects.get(pk=hostal_id)
    if request.method == 'POST':
        reg = forms.Reservacion(request.POST)

        hostal = str(reg['hostal'].value())

        asuntoCliente = "Solicitud recibida en Hostales-Nicaragua"
        mensajeCliente = "Pronto nos pondremos en contacto con usted. recibimos su solicitud para %s" % (hostal)
        para = str(reg['Email'].value())
        send_mail(asuntoCliente,mensajeCliente,'reservaenrealnicaragua@gmail.com',[para,],fail_silently=False,)

        return render(request,'hostal/detalles.html',{'para':para,'object':hosta})

    return render(request,'hostal/detalles.html',{'form':reg,'object':hosta})
    


