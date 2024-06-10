from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Flan, ContactForm
from .forms import ContactFormForm, LoginForm, ClientForm
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'lista_flanes': flanes_publicos}) # Flanes publicos-Index

def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    #request.session['name',] #capturar nombre de usuario
    private_flan = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flan_list': private_flan}) # Obtener los flanes privados

def customer(request):
    all_customer = models.Customer.objects.all() 
    context = {'customer':all_customer}
    return render(request,'customer.html',context=context)


def flan_list(request):
    all_flan = models.Flan.objects.all() 
    context = {'Flan':all_flan}
    return render(request,'flan.html',context=context)


def registration_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_client')  # Redirigir a una página de éxito
    else:
        form = ClientForm()
    return render(request, 'registration_form.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            ContactForm.objects.create(**form.cleaned_data)
            return redirect('success')
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirige a la página adecuada después del inicio de sesión exitoso
                return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'failed_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')  # o cualquier otra página a la que quieras redirigir después del logout