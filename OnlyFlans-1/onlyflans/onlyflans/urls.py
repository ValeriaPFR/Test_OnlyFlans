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
#import jazzmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('list/', views.customer, name='customer'),
    path('flan/', views.flan_list, name='flan_list'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('web.urls')),
    #path('admin/', include('jazzmin.urls')),  
]


