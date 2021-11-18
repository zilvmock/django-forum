from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as lgt
from django.contrib import messages
from django.utils.text import slugify
from posts.models import Author
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required
import os
from django.core.files.images import ImageFile

def signup(request):
    context = {}
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("profile")
    context.update({
        "form": form,
    })
    return render(request, './accounts/register.html', context)

def signin(request):
    context = {}
    form = LoginForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    context.update({
        "form": form,
    })
    return render(request, './accounts/login.html', context)

@login_required
def create_author(request):
    context = {}
    user = request.user
    author = Author

    form = ProfileForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            # profile.slug = slugify(request.POST['fullname'])
            # profile.fullname = request.POST['fullname']
            # profile.bio = request.POST['bio']
            # profile.profile_pic = request.POST['profile_pic']
            # author = profile
            profile.save()
            # messages.success(request, 'PAHITINO SITA MESSAGEEEEEEEE')
            return redirect("profile")

    try:
        author = Author.objects.get(user=request.user)
        if author is not None:
            is_author = True
            # form2 = ProfileForm(request.POST, request.FILES, instance=author, initial = {
            #     'fullname': author.fullname,
            #     'bio': author.bio,
            #     'profile_pic': author.profile_pic,
            # })
            # context2 = {
            #     "form": form2,
            # }
            # return render(request, './accounts/profile2.html', context)
            return redirect('profile2')
    except author.DoesNotExist:
        is_author = False
    # form = ProfileForm(initial = {
    #         'fullname': author.fullname,
    #         'bio': author.bio,
    #         'profile_pic': author.profile_pic,
    #         })
    context.update({
        "form": form,
        "is_author": is_author,
    })
    return render(request, './accounts/profile.html', context)

@login_required
def update_profile(request):
    context = {}
    user = request.user
    author = Author.objects.get(user=request.user)
    form = ProfileForm(request.POST, request.FILES, instance=author)
    if request.method == "POST":
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.slug = slugify(request.POST['fullname'])
            profile.fullname = request.POST['fullname']
            profile.bio = request.POST['bio']
            try:
                profile.profile_pic = request.FILES['profile_pic']
            except:
                if request.POST['profile_pic'] is None:
                    # tux = os.path("static/media/user_avatars/happy_tux.jpg")
                    f = ImageFile('static/media/user_avatars/happy_tux.jpg')
                    
                    profile.profile_pic = f
                # pass
                # PADARYTI KAD PASETINTU TUX JEIGU ISTRINI
                # if form.profile_pic.field.widget:
                #     profile.profile_pic = request.POST['profile_pic']
                # else:
                #     profile.profile_pic = author.profile_pic
                
                # profile.profile_pic = request.POST['profile_pic']
            profile.save()
            form = profile
            # messages.success(request, '22222222222')
            return redirect("home")
    
    form = ProfileForm(initial = {
        'fullname': author.fullname,
        'bio': author.bio,
        'profile_pic': author.profile_pic,
    })

    context.update({
        "form": form,
    })
    return render(request, './accounts/profile2.html', context)

@login_required
def logout(request):
    lgt(request)
    return redirect("home")