from django.contrib.auth import views as auth_views
from django.urls import path

from .views import register, profile, CustomLoginView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]