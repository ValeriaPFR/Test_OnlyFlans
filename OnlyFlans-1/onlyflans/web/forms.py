from django import forms
#from .models import ContactFormForm

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='email' )
    customer_name = forms.CharField(max_length=64, label='name' )
    message = forms.CharField(label='message' )