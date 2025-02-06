from django.shortcuts import render
from django.urls import get_resolver


def home(request):
    """Главная страница со списком всех URL-адресов"""

    return render(request, "home.html")
