from django.urls import path, include
from .views import (
    home, detail, posts, latest_posts,
    search_result,)

# app_name = 'posts'

urlpatterns = [
    # path('', include('forum.urls')),
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    # path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("search", search_result, name="search_result"),
]
