from django import forms

class Reservacion(forms.Form):
    Email = forms.EmailField(label = "Escriba su correo para contactarle, por favor.")
    hostal = forms.CharField()

    def __str__(self):
        return self.email

