from django.db import models

from usuario.models import Usuario

# Create your models here.
class Logro(models.Model):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id", null=False)
    titulo = models.CharField(verbose_name="Titulo")
    created_date = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    area = models.CharField(verbose_name="Area")
    descripcion = models.CharField(verbose_name="Descripcion")
    imagen = models.CharField(max_length=120, verbose_name="Imagen")
    status = models.BooleanField(default=True, verbose_name="Estatus")
    
    class Meta:
        db_table = 'logro'