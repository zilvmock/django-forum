from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import PostForm, UpdateForm
from django.contrib.auth.decorators import login_required


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
    }
    return render(request, './posts/index.html', context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    author = Author
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)
    
        if "post-a-comment" in request.POST:
            comment = request.POST.get("comment-content")
            new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
            post.comments.add(new_comment.id)

        if "post-a-reply" in request.POST:
            reply = request.POST.get("reply-content")
            comment_id = request.POST.get("comment-id")
            comment_obj = Comment.objects.get(id=comment_id)
            new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
            comment_obj.replies.add(new_reply.id)

    try:
        if author is not None:
            is_author = True
    except author.DoesNotExist:
        is_author = False
    
    context = {
        "post": post,
        "is_author": is_author,
    }
    update_views(request, post)

    return render(request, './posts/detail.html', context)


def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category, approved=True)
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
    }
    return render(request, './posts/posts.html', context)


@login_required
def create_post(request):
    author = Author
    try:
        author = Author.objects.get(user=request.user)
        if author is not None:
            is_author = True
    except author.DoesNotExist:
        is_author = False
    if is_author == False:
        return redirect("home")
    
    context = {}
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.slug = slugify(request.user.username + "-" + new_post.title)
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
    })
    return render(request, "./posts/create_post.html", context)

@login_required
def edit_post(request, slug):
    context = {}
    user = request.user
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = UpdateForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.slug = slugify(post.user.user.username + "-" + obj.title)
            obj.save()
            return redirect("home")
    
    form = UpdateForm(initial = {
        'title': post.title,
        'content': post.content,
        'tags': post.tags.all(),
    })

    context.update({
        "form": form,
    })
    return render(request, './posts/update_post.html', context)

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect("home")

def search_result(request):
    return render(request, "./posts/search.html")