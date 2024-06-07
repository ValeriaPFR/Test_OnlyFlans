from django.shortcuts import render
from . import models
from web.models import Flan, ContactForm
from .forms import ContactFormForm
from django.http import HttpResponseRedirect




# from .forms import ContactFormModelForm
# from .forms import CustomUserCreationForm
# from django.contrib.auth import authenticate
#from .models import ContactForm


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

#
def contact(request):
    #validar metodo post
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        #validar información correcta
        if form.is_valid():
            #guardado de la información en la base de datos
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            # redirección del metodo
            return HttpResponseRedirect('/success')

    else: 
        # redirección del metodo
        form = ContactFormForm()
            
    return render(request,'contact.html',{'form':form})

def success(request):
    return render(request, 'success.html')


