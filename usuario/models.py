from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=120, verbose_name="Nombre")
    fecha_nac = models.DateField(verbose_name="Fecha de Nacimiento")
    imagen = models.CharField(max_length=120, verbose_name="Imagen")
    
    
    email = models.EmailField(verbose_name="Correo Electrónico", unique=True)
    username = models.CharField(max_length=120, verbose_name="Usuario", unique=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','nombre','fecha_nac']
    
    def __str__(self):
        return self.email