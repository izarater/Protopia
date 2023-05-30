from mimetypes import init
from django.db import models 
from django.forms import IntegerField 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models import IntegerField, Model
from django.db.models import Avg
from django.db.models.deletion import CASCADE
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

import math


# Create your models here.

# class Puntuaciones(models.Model):
#     IdPuntuacion = models.AutoField(primary_key=True)
#     Puntuacion = models.IntegerField(default=0)


class Oficio(models.Model):
    NombreOficio= models.CharField(max_length=50,null=False,verbose_name="Oficio")
    IdOficio = models.AutoField(primary_key=True)
    def __str__(self):
        return self.NombreOficio
class Contacto(models.Model):
    IdContacto = models.AutoField(primary_key=True)
    Nombre= models.CharField(max_length=100, null=False, verbose_name="Nombre")
    Telefono= models.CharField(verbose_name="Teléfono",max_length=12)
    Direccion = models.CharField(max_length=100,null=False,verbose_name="Dirección") 
    Barrio = models.CharField(max_length=100,null=False,verbose_name="Barrio") 
    Municipio = models.CharField(max_length=100,null=False,verbose_name="Municipio") 
    xCoor = models.FloatField(null=False,verbose_name="Latitud (x)")
    yCoor = models.FloatField(null=False,verbose_name="Longitud (y)")
    IdCreador =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Oficios = models.ManyToManyField(Oficio, verbose_name=("Oficio(s)"))
    Descripcion = models.TextField(null=False,verbose_name="Descripción") 
    Ubicación = models.CharField(max_length=100, null=False)
    nombresoficios = models.CharField(max_length=300,null=False)

    def save(self, *args, **kwargs):
        self.Ubicación = '(' + str(self.xCoor) + ', ' + str(self.yCoor) + ')'
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f"{self.Nombre}"
    
@receiver(m2m_changed, sender=Contacto.Oficios.through)
def update_oficios_names(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        instance.nombresoficios = ", ".join([of.NombreOficio for of in instance.Oficios.all()])
        instance.save()