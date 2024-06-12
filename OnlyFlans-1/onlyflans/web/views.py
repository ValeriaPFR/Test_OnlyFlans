from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .models import Flan, ContactForm, Client
from .forms import ContactFormForm, LoginForm, ClientFormForm #, FlanFormForm



def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'lista_flanes': flanes_publicos}) # Flanes publicos-Index

def flan_list(request):
    all_flan = Flan.objects.all() 
    context = {'Flan':all_flan}
    return render(request,'flan.html',context=context)

def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'registration/new_client/welcome.html')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return render(request, 'index.html')
    else:
        #request.session['name',] #capturar nombre de usuario
        private_flan = Flan.objects.filter(is_private=True)
        return render(request, 'welcome.html', {'flan_list': private_flan}) # Obtener los flanes privados

def add_group_client(request, cliente_id):
    client = Client.objects.get(pk="name")
    group = Group.objects.get(name="Cliente")
    
    # Agregar el cliente al grupo
    client.groups.add(group)
    
    return HttpResponse("Cliente agregado al grupo exitosamente")

def registration_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            Client.objects.create(**form.cleaned_data)
            return redirect('welcome')  # Redirige a la página de bienvenida
    else:
        form = ClientForm()
    return render(request, 'registration_form.html', {'form': form})


# def welcome_view(request):
#     return render(request, 'welcome.html')

def new_client(request):
    return render(request, 'registration/new_client.html')

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
                return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'welcome.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')  # Redirigir a la página de bienvenida
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')  