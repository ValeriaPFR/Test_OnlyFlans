from django import forms
#from .models import ContactFormForm

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='email' )
    customer_name = forms.CharField(max_length=64, label='name' )
    message = forms.CharField(label='message' )
    

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length= 64, label="Nombre")
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     email = forms.EmailField(label = 'Email')

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )