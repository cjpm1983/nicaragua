from django import forms

class Reservacion(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.email

