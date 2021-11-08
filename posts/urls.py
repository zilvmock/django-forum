from django.urls import path, include
from .views import homepage_view, detail_view, posts_view

app_name = 'posts'

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('detail/<slug>/', detail_view, name='detail'),
    path('posts/', posts_view, name='posts'),
]
