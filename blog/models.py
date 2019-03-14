from django.db import models
# Manejo de Fechas
from django.utils.timezone import now
# Acceso a usuarios
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")

    class Meta: 
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["-created"]  

    def __str__(self):
        return "%s %s" % (self.name, self.created)


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    content = models.TextField(verbose_name = "Contenido")
    published = models.DateTimeField(verbose_name = "Fecha de Publicación", default=now)
    image = models.ImageField(verbose_name = "Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name = "Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name = "categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"] 
