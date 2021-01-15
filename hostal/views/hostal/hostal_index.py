# from django.views.generic import ListView

# from hostal.models import Hostal

# class HostalIndexView(ListView):
#     model = Hostal
#     template_name = "hostal/index.html"

from django.shortcuts import render
from django.core.mail import send_mail
from reservacion import forms

from hostal.models import Hostal

def HostalIndexView(request):

    reg = forms.Reservacion()

    #hosta = Hostal.objects.get(pk=hostal_id)
    if request.method == 'POST':
        reg = forms.Reservacion(request.POST)

        #hostal = str(reg['hostal'].value())

        asuntoCliente = "Solicitud recibida en Hostales-Nicaragua"
        mensajeCliente = "Pronto nos pondremos en contacto con usted. recibimos su solicitud para %s" % ("RealNicaragua")
        para = str(reg['Email'].value())
        send_mail(asuntoCliente,mensajeCliente,'reservaenrealnicaragua@gmail.com',[para,],fail_silently=False,)

        return render(request,'hostal/index.html',{'para':para})

    return render(request,'hostal/index.html',{'form':reg})
    


