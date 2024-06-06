from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from web.models import Flan, ContactForm

# from .forms import ContactFormModelForm
# from .forms import CustomUserCreationForm
# from django.contrib.auth import authenticate
# from .models import ContactForm


# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'lista_flanes': flanes_publicos}) # Flanes publicos-Index

def about(request):
    return render(request, 'about.html', {})

def welcome(request):
    #request.session['name',] #capturar nombre de usuario
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'lista_flanes': flanes_privados}) # Obtener los flanes privados

def lista_clientes(request):
    todos_clientes = models.Cliente.objects.all() 
    context = {'clientes':todos_clientes}
    return render(request,'list.html',context=context)


def lista_flanes(request):

    todos_flanes = models.Flan.objects.all() 
    context = {'Flan':todos_flanes}
    return render(request,'flan.html',context=context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']

            messages.success(request, 'El mensaje se ha enviado correctamente.')
            return redirect('success')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')


