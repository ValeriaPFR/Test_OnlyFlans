from django.shortcuts import render, redirect
from . import models
from web.models import Flan, ContactForm
from .forms import ContactFormForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages




#from django.http import HttpResponseRedirect

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

@login_required
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
            #return HttpResponseRedirect('/success')
            return redirect('/success')

    else: 
        # redirección del metodo
        form = ContactFormForm()
    return render(request,'contact.html',{'form':form})

def success(request):
    return render(request, 'success.html') 

# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     #validar metodo post
#     if request.method == 'POST':
#         form = LoginForm(request.POST) #se le pasa todo el post y como es un form, captura solo 
#         if form.is_valid(): #si el form esta bien
#             #se inserta
#             LoginForm.objects.create(**form.cleaned_data) #se hace una insercion con los datos del form, limpios.
            
#         return redirect('welcome')
    
# def logout(rewquest):
#     return redirect('logout')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio o a donde prefieras
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def some_protected_view(request):
    # Código para una vista que requiere que el usuario esté autenticado
    return render(request, 'welcome.html')
