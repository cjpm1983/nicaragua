from django import forms
#from .widgets import BootstrapDateTimePickerInput
from .models import Aerolinea

airlines=[]
for a in Aerolinea.objects.all():
    t = (a.Nombre,a.Nombre)
    airlines.append(t)

class Reservacion(forms.Form):
    Nombre = forms.CharField(required=True, max_length=200,help_text="Entre su nombre y apellidos tal y como aparecen en su pasaporte", error_messages={'required': 'Por favor,entre su nombre y apellidos.'})
    Pasaporte = forms.CharField(max_length=7,min_length=7,required=True,error_messages={'required':"Entre un valor validode 7 digitos de su pasaporte cubano"})
    Email = forms.EmailField(label = "Su correo electrónico")
    Personas = forms.ChoiceField(label="Habitación para",choices=[(1,"Una persona"),(2,"Dos personas")] )
    HoraEntrada = forms.DateTimeField(label="Día y hora de entrada",input_formats=['%d/%m/%Y %H:%M'])
    HoraSalida = forms.DateTimeField(label="Día y hora de salida",input_formats=['%d/%m/%Y %H:%M'])
    Aerolinea = forms.ChoiceField(label="Aerolínea",choices=airlines )
    Observaciones = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':30,"class":'md-textarea'}))
    Imagen_Pasaporte = forms.ImageField(required=True,help_text="Foto de la primera hoja del pasaporte")
    Imagen_Pasaje = forms.ImageField(required=False,help_text="Foto del pasaje")

    def __str__(self):
        return self.email

