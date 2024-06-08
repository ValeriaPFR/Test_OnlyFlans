from django.contrib import admin
from .models import Cliente, Flan
from .models import ContactForm

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'age', 'subject', 'message')


@admin.register(Flan)# o admin.site.register(Flan) 
class FlanAdmin(admin.ModelAdmin):
    list_display = ('flan_id', 'name', 'description', 'preparation', 'ingredients', 'img_url', 'slug', 'is_private' )


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'customer_name', 'message')
    