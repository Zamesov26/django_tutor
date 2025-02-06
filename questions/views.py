from random import randint

from django.shortcuts import render, redirect, get_object_or_404

from questions.tasks import play_sound_task
from .forms import AnswerForm, QuestionForm
from .models import Question


def add_question(request):
    """Форма для добавления нового вопроса"""
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("question_list")
    else:
        form = QuestionForm()
    return render(request, "add_question.html", {"form": form})


def question_list(request):
    """Выводит только список вопросов (без ответов)"""
    questions = Question.objects.order_by("-created_at")
    return render(request, "question_list.html", {"questions": questions})


def question_detail(request, question_id):
    """Просмотр конкретного вопроса с его ответами"""
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.order_by("-created_at")
    return render(
        request, "question_detail.html", {"question": question, "answers": answers}
    )


def add_answer(request, question_id):
    """Форма для добавления ответа к вопросу"""
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("question_detail", question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, "add_answer.html", {"form": form, "question": question})


def send_sound(request, question_id):
    """Создаёт задачу в Celery для воспроизведения звука"""
    play_sound_task.apply_async(args=[1])  # Запускаем задачу в Celery
    return redirect("question_list")
