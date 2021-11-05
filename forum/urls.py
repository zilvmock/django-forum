from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'forum'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace="posts")),
    # path('/', views.redirect_to_homepage),
    # path('main/', views.homepage_view, name='homepage'),
]
