from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
import uuid




# Create your models here.
class Cliente(models.Model):
    
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, default="cliente@cliente.cl") 
    age= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)],default=18)
    subject = models.CharField(max_length=200, default="")
    message = models.TextField(max_length=1000, default="") 
    
# Create your models here.
class Flan(models.Model):
    flan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=64) #Nombre del flan ej. Flan de ...
    description = models.TextField() #Regular o Light
    preparation = models.TextField() 
    ingredients = models.TextField()
    img_url = models.URLField(max_length=200)#
    slug = models.SlugField() #flan_de_...
    is_private = models.BooleanField() #Premium/No Premium
    #atributo de fecha-hora en la creacion de registros
    
    
    #info entregada por el profesor
    created_at= models.DateTimeField(auto_now_add=True)#Registro en el momento del ingreso
    #atributo fecha-hora en la modificacion de registro
    updated_at= models.DateTimeField(auto_now=True)
    #deleted_at=> muestra los registros que fueron eliminados
    #Todas las columnas de fecha sirven para realizar reportes
    #Están registrados en la base de datos
    
    def __str__(self):
        return f"El {self.name} {self.img_url} es {self.description} "
    
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False) 
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    #revisar en la base de datos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.customer_email} - Mensaje: {self.message}"
    

