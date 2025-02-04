from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm

def question_list(request):
    """Выводит список всех вопросов"""
    questions = Question.objects.all().order_by("-created_at")
    return render(request, "questions/question_list.html", {"questions": questions})

def add_question(request):
    """Форма для добавления нового вопроса"""
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("question_list")
    else:
        form = QuestionForm()
    return render(request, "questions/add_question.html", {"form": form})

