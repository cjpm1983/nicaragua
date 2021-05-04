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
    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"

    def __str__(self):
        return self.nombre

class Aerolinea(models.Model):
    Nombre = models.CharField(max_length=100,null=False)
    Descripcion = models.TextField()
    def __str__(self):
        return self.Nombre

class Reservacion(models.Model):
    # Nombre = models.CharField(max_length=200,null=False)
    # Pasaporte = models.CharField(max_length=7,null=False)
    # Email = models.EmailField()
    # Imagen_Pasaporte = ResizedImageField(upload_to="reservaciones/pasaportes", null=True, blank=True)
    # Imagen_Pasaje = ResizedImageField(upload_to="reservaciones/pasaje", null=True, blank=True)

    aNombre=models.ForeignKey("hostal.Cliente", verbose_name=("A nombre de"), on_delete=models.CASCADE,blank=True,null=True)
    Personas = models.IntegerField(null=True)
    HoraEntrada = models.DateTimeField(verbose_name=("Fecha y hora de entrada"))
    HoraSalida = models.DateTimeField(verbose_name=("Fecha y hora de entrada"))
    #Aerolinea = models.CharField(max_length=200,null=True)
    Aerolinea = models.ForeignKey(Aerolinea,on_delete=models.DO_NOTHING,null=True)
    Reservado_Por = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    #imagendestacada = models.ImageField(upload_to="imageshostales", null=True, blank=True)
    pdf = models.CharField(max_length=200, null=True)
    Observaciones = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=("Fecha de creada"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=("Fecha de actualizada"))
    class Meta:
        verbose_name = "Reservación"
        verbose_name_plural = "Reservaciones"
    def __str__(self):
        return '%s_%s_%s-personas_%s'%(self.aNombre,self.Aerolinea,self.Personas,self.HoraEntrada)

class Cliente(models.Model):
    Nombre = models.CharField(max_length=200,null=False)
    Pasaporte = models.CharField(max_length=7,null=False)
    Email = models.EmailField()
    Imagen_Pasaporte = ResizedImageField(upload_to="reservaciones/pasaportes", null=True, blank=True)
    Imagen_Pasaje = ResizedImageField(upload_to="reservaciones/pasaje", null=True, blank=True)
    Reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=("Fecha de creado"))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=("Fecha de actualizado"))
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.Nombre

    