from django.shortcuts import render, get_object_or_404
# Se agrega el modelo
from .models import Post, Category

# Create your views here.
def blog(request):
    # Con el ORM de Django se obtienen los datos en objetos
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # posts = Post.objects.filter(categories=category)
    # return render(request, "blog/category.html", {'category':category, 'posts':posts})
    return render(request, "blog/category.html", {'category':category})
