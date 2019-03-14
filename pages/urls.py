from django.urls import path
# Importo las vistas que estan en este directorio
from . import views

urlpatterns = [
    path('<int:page_id>/', views.page, name='page'),
]
