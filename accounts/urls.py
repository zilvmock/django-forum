from django.urls import path
from .views import signup, signin, logout, create_author, update_profile


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("logout/", logout, name="logout"),
    path("profile/", create_author, name="profile"),
    path("profile-update/", update_profile, name="profile2"),
]
