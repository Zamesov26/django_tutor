from django.urls import path

from django_tutor.base.views import home

urlpatterns = [
    path("", home, name="home"),
]
