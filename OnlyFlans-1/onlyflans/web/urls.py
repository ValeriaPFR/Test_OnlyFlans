from django.urls import path
from . import views
from .views import registration_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('login/', views.user_login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.user_logout, name='logout'),
    path('client/', views.Client, name='client'),
    path('register/', registration_view, name='registration_form'),
    path('new_client/', views.new_client_view, name='new_client'),
    path('welcome/', views.welcome, name='welcome'),
]
