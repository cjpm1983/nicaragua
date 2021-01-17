from django.shortcuts import render
from django.core.mail import send_mail
from hostal import forms

from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from hostales.settings import MEDIA_ROOT as mediadir
import os
import datetime
from django.contrib.auth.decorators import login_required

from hostal.models import Hostal

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
        
        send_mail(asuntoCliente,mensajeCliente,'reservaenrealnicaragua@gmail.com',[para,],fail_silently=False,)


        #Generacion del PDF
            # Rendered
        html_string = render_to_string('hostal/pdf.html', {'nombre': "Carlos Palacios"})
        html = HTML(string=html_string)
        archivo = datetime.datetime.now()
        salida = os.path.join(mediadir, "hostal","static","pdfs",'%s_%s.pdf'%(para,archivo))
        result = html.write_pdf(salida)
        
        #Fin delpdf

        return render(request,'hostal/reservar.html',{'form':reg,'para':para})

    return render(request,'hostal/reservar.html',{'form':reg})
    


