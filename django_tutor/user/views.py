from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(request):
    """Регистрация нового пользователя"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

@login_required(login_url="/login")
def profile(request):
    """Страница профиля пользователя"""
    return render(request, "profile.html")

class CustomLoginView(LoginView):
    """Перенаправляет авторизованных пользователей на главную"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")  # Перенаправляем на главную
        return super().dispatch(request, *args, **kwargs)