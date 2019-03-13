from django.contrib import admin
# Crear administrador para nuestro Blog
from .models import Category, Post

# Se extiende la configuracion del modelo para su administracion
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # list_display = ('title', 'author', 'published')
    # Mostrar un campo desde una relacion
    list_display = ('title', 'author', 'published', 'post_categories')
    # Siempre dejarlo con una , porque espera una tupla
    ordering = ('author', 'published') 
    search_fields = ('title', 'content', 'author__username', 'categories__name') 
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
