"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web import views
from web.views import index, about, welcome, contact, success, login




urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('welcome/', welcome, name='welcome'),
    path('list/',views.lista_clientes,name='lista_clientes'),
    path('flan/', views.lista_flanes, name='lista_flanes'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('login/', user_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('login', login, name='login') #no va pq se ocupa el de accounts
    
]


