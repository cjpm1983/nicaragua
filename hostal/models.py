from django.db import models
from usuario.models import UserProfile 
from django_resized import ResizedImageField

# Create your models here.


class Hostal(models.Model):
    nombre = models.CharField(max_length=100)
    
    resumen = models.TextField()
    descripcion = models.TextField()
    direccion = models.TextField()
    imagendestacada = models.ImageField(upload_to="imageshostales", null=False, blank=False)

    def __str__(self):
        return self.nombre

class Aerolinea(models.Model):
    Nombre = models.CharField(max_length=100,null=False)
    Descripcion = models.TextField()
    def __str__(self):
        return self.Nombre

class Reservacion(models.Model):
    Nombre = models.CharField(max_length=200,null=False)
    Pasaporte = models.CharField(max_length=12,null=False)
    Email = models.EmailField()
    Personas = models.IntegerField(null=True)
    HoraEntrada = models.DateTimeField()
    HoraSalida = models.DateTimeField()
    #Aerolinea = models.CharField(max_length=200,null=True)
    Aerolinea = models.ForeignKey(Aerolinea,on_delete=models.DO_NOTHING,null=True)
    Reservado_Por = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    #imagendestacada = models.ImageField(upload_to="imageshostales", null=True, blank=True)
    pdf = models.CharField(max_length=200, null=True)
    Observaciones = models.TextField(null=True)
    Imagen_Pasaporte = ResizedImageField(upload_to="reservaciones/pasaportes", null=True, blank=True)
    Imagen_Pasaje = ResizedImageField(upload_to="reservaciones/pasaje", null=True, blank=True)
    def __str__(self):
        return self.Nombre

    