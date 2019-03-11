from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at Inicio home/")

def about(request):
    return HttpResponse("Hello, world. You're at Historia about/")

def services(request):
    return HttpResponse("Hello, world. You're at Servicios services/")

def store(request):
    return HttpResponse("Hello, world. You're at Visítanos store/")

def contact(request):
    return HttpResponse("Hello, world. You're at Contacto contact/")

def blog(request):
    return HttpResponse("Hello, world. You're at Blog blog/")

def sample(request):
    return HttpResponse("Hello, world. You're at Sample sample/ (esta es para páginas de prueba)")
