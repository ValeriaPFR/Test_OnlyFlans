from django.contrib import admin
from .models import Client, Flan, ContactForm
from .models import ContactForm

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'age', 'subject', 'message', 'birth_date', 'address', 'created_at', 'updated_at')


@admin.register(Flan)# o admin.site.register(Flan) 
class FlanAdmin(admin.ModelAdmin):
    list_display = ('flan_id', 'name', 'description', 'preparation', 'ingredients', 'img_url', 'slug', 'is_private' )

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'message', 'created_at', 'updated_at')
    
