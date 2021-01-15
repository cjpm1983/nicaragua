from django import forms

class Reservacion(forms.Form):
    Nombre = forms.CharField(max_length=200,required=True,help_text="Entre su nombre y apellidos tal y como aparecen en su pasaporte", error_messages={'required': 'Por favor,entre su nombre y apellidos.'})
    Pasaporte = forms.CharField(max_length=7,min_length=7,required=True,help_text="Entre un valor validode 7 digitos de su pasaporte cubano")
    Email = forms.EmailField(label = "Escriba su correo para contactarle, por favor.")
    FechaEntrada = forms.DateField(required=True, widget=forms.SelectDateWidget)
    HoraEntrada =  forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget)
    Aerolinea = forms.ChoiceField(choices=[("UA","United Airlines"),("AA","American Airlines")])
    def __str__(self):
        return self.email

