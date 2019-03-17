from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Hello, world. You're at Inicio home/")
    return render(request, "core/home.html")

def about(request):
    #return HttpResponse("Hello, world. You're at Historia about/")
    return render(request, "core/about.html")

""" def services(request):
    #return HttpResponse("Hello, world. You're at Servicios services/")
    return render(request, "core/services.html") """

def store(request):
    #return HttpResponse("Hello, world. You're at Visítanos store/")
    return render(request, "core/store.html")

""" def contact(request):
    #return HttpResponse("Hello, world. You're at Contacto contact/")
    return render(request, "core/contact.html") """

""" def blog(request):
    #return HttpResponse("Hello, world. You're at Blog blog/")
    return render(request, "core/blog.html") """

""" def sample(request):
    return HttpResponse("Hello, world. You're at Sample sample/ (esta es para páginas de prueba)") """
