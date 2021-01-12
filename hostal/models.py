from django.db import models

# Create your models here.

class Hostal(models.Model):
    nombre = models.CharField(max_length=100)
    
    resumen = models.TextField()
    descripcion = models.TextField()
    direccion = models.TextField()
    imagendestacada = models.ImageField(upload_to="imageshostales", null=False, blank=False)

    def __str__(self):
        return self.nombre