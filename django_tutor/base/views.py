from django.shortcuts import render


def home(request):
    """Главная страница со списком всех URL-адресов"""

    return render(request, "home.html")
