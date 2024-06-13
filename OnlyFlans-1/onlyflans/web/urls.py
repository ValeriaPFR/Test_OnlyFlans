#Rutas específicas de la aplicación
from django.urls import path
from . import views
from .views import registration_view, login
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/', login, name='login'),
    path('logout/', views.user_login, name='logout'),
    path('client/', views.Client, name='client'),
    path('register/', views.registration_view, name='registration'),
    path('new_client/', views.new_client, name='new_client'),
]
