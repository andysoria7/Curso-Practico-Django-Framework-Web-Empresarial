from django.shortcuts import render, get_object_or_404 # Evita el error "DoesNotExit" y en su lugar muestra "Page not found".
from .models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id) # El get nos permite recoger un unico registro filtrando por una serie de campos.
    return render(request, "blog/category.html", {'category':category})
    
    