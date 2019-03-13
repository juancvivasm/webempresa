from django.shortcuts import render
# Se agrega el modelo
from .models import Post

# Create your views here.
def blog(request):
    # Con el ORM de Django se obtienen los datos en objetos
    posts = Post.objects.all()

    return render(request, "blog/blog.html", {'posts':posts})
