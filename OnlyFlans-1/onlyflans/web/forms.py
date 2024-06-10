from django import forms
from .models import Client

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Email')
    customer_name = forms.CharField(max_length=64, label='Name')
    message = forms.CharField(label='Message')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label="Nombre")
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'lastname', 'email', 'age', 'subject', 'message']