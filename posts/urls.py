from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
]
