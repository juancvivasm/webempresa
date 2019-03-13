from django.shortcuts import render
# Se agrega el modelo
from .models import Service

# Create your views here.
def services(request):
    # Con el ORM de Django se obtienen los datos en objetos
    services = Service.objects.all()
    
    return render(request, "services/services.html", {'services':services})
