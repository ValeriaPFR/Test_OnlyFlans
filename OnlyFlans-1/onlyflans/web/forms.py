from django import forms
#from .models import ContactFormForm

class ContactFormForm(forms.Form):
    email = forms.EmailField(label='email' )
    name = forms.CharField(max_length=64, label='name' )
    message = forms.CharField(label='message' )