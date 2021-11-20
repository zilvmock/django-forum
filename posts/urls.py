from django.urls import path, include
from .views import home, detail, posts, create_post, delete_post, edit_post, search_result

urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path('account/', include('accounts.urls')),
    path("create-post/", create_post, name="create-post"),
    path("search/", search_result, name="search"),
    path("edit/<slug>/", edit_post, name="edit-post"),
    path("delete/<slug>/", delete_post, name="delete-post"),
]
