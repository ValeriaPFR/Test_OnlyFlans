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
    path('list/', views.customer, name='customer'),
    path('flan/', views.flan_list, name='flan_list'),
    path('register/', registration_view, name='registration_view'),
    path('new_client/', TemplateView.as_view(template_name="new_client.html"), name='success_view'),
]
