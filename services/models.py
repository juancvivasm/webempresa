from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    subtitle = models.CharField(max_length=200, verbose_name = "Subtítulo ")
    content = models.TextField()
    image = models.ImageField(verbose_name = "Imagen", upload_to="services" )
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")
