from django.db import models
from django.utils import timezone

# Create your models here.
# Creación de campos de la tabla 'postres' 
class Postres(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'postres' # Le doy de nombre 'postres' a nuestra tabla en la Base de Datos 