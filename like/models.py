from django.db import models

from usuario.models import Usuario
from logro.models import Logro

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id", null=False)
    logro = models.ForeignKey(Logro, on_delete=models.CASCADE, verbose_name="logro")
    created_date = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    status = models.BooleanField(default=True, verbose_name="Estatus")
    
    class Meta:
        db_table = 'like'
        unique_together = ('user', 'logro')  # Un usuario puede dar un like a un logro solo una vez
    