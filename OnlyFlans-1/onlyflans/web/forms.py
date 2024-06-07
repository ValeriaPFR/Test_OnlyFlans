from django import forms
#from .models import ContactFormForm

class ContactFormForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico' )
    name = forms.CharField(max_length=64, label='Nombre' )
    message = forms.CharField(label='Mensaje' )