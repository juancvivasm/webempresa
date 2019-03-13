from django.contrib import admin
# Crear administrador para nuestro Blog
from .models import Category, Post

# Se extiende la configuracion del modelo para su administracion
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
