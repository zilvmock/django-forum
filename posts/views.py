from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
from .utils import update_views

from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    categories = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = categories.count()
    
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []

    context = {
        "categories": categories,
        "num_posts": num_posts,
        "num_users": num_users,
        "num_categories": num_categories,
        "last_post": last_post,
        "title": "OZONE forum app"
    }

    return render(request, './posts/index.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        commenr_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=commenr_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
        comment_obj.replies.add(new_reply.id)


    context = {
        "post":post,
        "title": "OZONE: "+post.title,
    }
    update_views(request, post)

    return render(request, './posts/detail.html', context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    context = {
        "posts":posts,
        "category": category,
        "title": "OZONE: Posts"
    }

    return render(request, './posts/posts.html', context)



# def create_post(request):
#     context = {}
#     # form = PostForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             print("\n\n its valid")
#             author = Author.objects.get(user=request.user)
#             new_post = form.save(commit=False)
#             new_post.user = author
#             new_post.save()
#             form.save_m2m()
#             return redirect("home")
#     context.update({
#         "form": form,
#         "title": "OZONE: Create New Post"
#     })
#     return render(request, "create_post.html", context)

def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "OZONE: Latest 10 Posts"
    }

    return render(request, "latest-posts.html", context)

def search_result(request):

    return render(request, "search.html")