from django.urls import path
# Importo las vistas que estan en este directorio
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
]
