from django import forms
#from .widgets import BootstrapDateTimePickerInput


class Reservacion(forms.Form):
    Nombre = forms.CharField(max_length=200,required=True,help_text="Entre su nombre y apellidos tal y como aparecen en su pasaporte", error_messages={'required': 'Por favor,entre su nombre y apellidos.'})
    Pasaporte = forms.CharField(max_length=7,min_length=7,required=True,error_messages={'required':"Entre un valor validode 7 digitos de su pasaporte cubano"})
    Email = forms.EmailField(label = "Su correo electrónico")
    Personas = forms.ChoiceField(label="Habitación para",choices=[(1,"Una persona"),(2,"Dos personas")] )
    HoraEntrada = forms.DateTimeField(label="Día y hora de entrada",input_formats=['%d/%m/%Y %H:%M'])
    HoraSalida = forms.DateTimeField(label="Día y hora de salida",input_formats=['%d/%m/%Y %H:%M'])
    Aerolinea = forms.ChoiceField(label="Aerolínea",choices=[("United Airlines","United Airlines"),("American Airlines","American Airlines")] )
    def __str__(self):
        return self.email

