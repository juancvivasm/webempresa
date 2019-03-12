from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    subtitle = models.CharField(max_length=200, verbose_name = "Subtítulo ")
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(verbose_name = "Imagen", upload_to="services" )
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")
    
    class Meta: 
        ordering = ["-created"]  
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return '%s %s' % (self.title, self.created)
