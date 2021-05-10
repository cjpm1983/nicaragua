from django.shortcuts import render
from django.core.mail import send_mail
from hostal import forms
from hostal.models import Reservacion, Aerolinea, Cliente

from django.template.loader import render_to_string
from weasyprint import HTML, CSS
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
        
        reg = forms.Reservacion(request.POST or None, request.FILES or None)
        if reg.is_valid():
        #hostal = str(reg['hostal'].value())

            asuntoCliente = "Solicitud recibida en Hostales-Nicaragua"
            mensajeCliente = "Pronto nos pondremos en contacto con usted. recibimos su solicitud para %s" % ("RealNicaragua")
            para = str(reg['Email'].value())
            
            #send_mail(asuntoCliente,mensajeCliente,'reservaenrealnicaragua@gmail.com',[para,],fail_silently=False,)

            #Nombre para el PDF
            archivo = "%s_%s"% (str(reg['Pasaporte'].value()),datetime.datetime.now())

            airline = Aerolinea.objects.filter(Nombre=str(reg['Aerolinea'].value()))

 


            #Crear Reservacion sin aNombre de
            R = Reservacion(
                # Nombre=str(reg['Nombre'].value()),
                # Email=str(reg['Email'].value()),
                Personas=str(reg['Personas'].value()),
                # Pasaporte=str(reg['Pasaporte'].value()),

                #aNombre=aNombre,

                HoraEntrada=str(reg['HoraEntrada'].value()),
                HoraSalida=str(reg['HoraSalida'].value()),
                Observaciones=reg.cleaned_data['Observaciones'],
                Aerolinea=airline[0],
                Reservado_Por=request.user,
                pdf='%s_%s.pdf'%(para,archivo),
                # Imagen_Pasaporte = reg.cleaned_data['Imagen_Pasaporte'],
                # Imagen_Pasaje = reg.cleaned_data['Imagen_Pasaje'],
            )
            R.save()
            #Creamos aNombre de y lo agregamos
            aNombre=Cliente(
                Nombre=str(reg['Nombre'].value()),
                Email=str(reg['Email'].value()),
                Pasaporte=str(reg['Pasaporte'].value()),
                Imagen_Pasaporte = reg.cleaned_data['Imagen_Pasaporte'],
                Imagen_Pasaje = reg.cleaned_data['Imagen_Pasaje'],
                Reservacion=R
                )
            aNombre.save()
            #Agragdo aNombre de a Reservacion
            R.aNombre=aNombre
            R.save()

            #dias para el pdf
            fe = datetime.datetime.strptime(R.HoraEntrada,"%Y-%m-%d %H:%M") 
            fs = datetime.datetime.strptime(R.HoraSalida,"%Y-%m-%d %H:%M") 
            dias = (fs - fe).days
            #- datetime(reg['HoraSalida'].value())  )

            #Agregando los extras
            extras = []
            if 'Nombrel[]' in request.POST:
                print(request.FILES)

                Nombrel = request.POST.getlist('Nombrel[]')
                Pasaportel = request.POST.getlist('Pasaportel[]')
                Imagen_Pasaportel = request.FILES.getlist('Imagen_Pasaportel[]')
                Imagen_Pasajel = request.FILES.getlist('Imagen_Pasajel[]')

                for i in range(0, len(Nombrel)):
                    c = Cliente(Nombre=Nombrel[i],
                                Reservacion=R,
                                Pasaporte=Pasaportel[i],
                                Imagen_Pasaporte=Imagen_Pasaportel[i],
                                Imagen_Pasaje=Imagen_Pasajel[i] 
                                )
                    c.save()
                    # los demas clientes para el pdf
                    extras.append(c)
            
            pagototal = dias*20*(len(extras) + 1) + 10                   


            
            # tipo = request.POST['tipo']
            # te = str(reg['Nombrel'][0].value()),

            # print("Se salvo%s"%te)

            # Generacion del PDF
                # Rendered
            html_string = render_to_string('hostal/reserva.html', {'t':pagototal, 'fe':fe, 'fs':fs, 'r': R, 'dias': dias, 'aNombre': aNombre, 'agente': request.user, 'extras': extras})
            html = HTML(string=html_string)
            
            salida = os.path.join(mediadir, "hostal", "static", "pdfs", '%s_%s.pdf' % (para, archivo))
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
    


