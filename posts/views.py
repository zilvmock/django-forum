from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post

def homepage_view(request):
    # post = get_object_or_404(Post)
    all_posts = Post.objects.all()
    all_categories = Category.objects.all()
    context = {
        'posts': all_posts,
        'categories': all_categories,
    }

    return render(request, 'posts/index.html', context)

def detail_view(request, slug):

    return render(request, 'posts/detail.html')

def posts_view(request):
    
    return render(request, 'posts/post.html')