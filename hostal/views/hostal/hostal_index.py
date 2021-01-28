from django.shortcuts import render
from django.core.mail import send_mail
from hostal import forms
from hostal.models import Reservacion

from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from hostales.settings import MEDIA_ROOT as mediadir
import os
import datetime
from django.contrib.auth.decorators import login_required

from hostal.models import Hostal

from django.core.mail import EmailMessage

@login_required(login_url="")
def HostalIndexView(request):

    reg = forms.Reservacion()

    #hosta = Hostal.objects.get(pk=hostal_id)
    if request.method == 'POST':
        reg = forms.Reservacion(request.POST)

        #hostal = str(reg['hostal'].value())

        asuntoCliente = "Solicitud recibida en Hostales-Nicaragua"
        mensajeCliente = "Pronto nos pondremos en contacto con usted. recibimos su solicitud para %s" % ("RealNicaragua")
        para = str(reg['Email'].value())
        
        #send_mail(asuntoCliente,mensajeCliente,'reservaenrealnicaragua@gmail.com',[para,],fail_silently=False,)

        #Nombre para el PDF
        archivo = "%s_%s"% (str(reg['Pasaporte'].value()),datetime.datetime.now())

        #Crear Reservacion
        R = Reservacion(
        Nombre=str(reg['Nombre'].value()),
        Email=str(reg['Email'].value()),
        Personas=str(reg['Personas'].value()),
        Pasaporte=str(reg['Pasaporte'].value()),
        HoraEntrada=str(reg['HoraEntrada'].value()),
        HoraSalida=str(reg['HoraSalida'].value()),
        Aerolinea=str(reg['Aerolinea'].value()),
        Reservado_Por=request.user,
        pdf='%s_%s.pdf'%(para,archivo),
        )
        R.save()

        #Generacion del PDF
            # Rendered
        html_string = render_to_string('hostal/pdf.html', {'reservacion': R,'usuario':request.user})
        html = HTML(string=html_string)
        
        salida = os.path.join(mediadir, "hostal","static","pdfs",'%s_%s.pdf'%(para,archivo))
        result = html.write_pdf(salida)
        
        email = EmailMessage(
            "Hotel Real - Confirmación de Reservación",
            mensajeCliente,
            'reservaenrealnicaragua@gmail.com',
            [para,],
        )
        email.content_subtype='html'
        email.attach_file(salida)
        email.send(fail_silently=False)





        #Fin delpdf

        return render(request,'hostal/reservar.html',{'form':reg,'para':para})

    return render(request,'hostal/reservar.html',{'form':reg})
    


