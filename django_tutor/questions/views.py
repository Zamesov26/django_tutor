from django.shortcuts import render, redirect, get_object_or_404

from .forms import AnswerForm, QuestionForm, TagForm
from .models import Question, Tag


def add_question(request):
    """Форма для добавления нового вопроса"""
    selected_tags = request.GET.get("tags", "")
    selected_tags = list(map(int, selected_tags.split(","))) if selected_tags else []

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # Сохраняем вопрос без тегов
            question.save()
            form.save_m2m()  # Сохраняем выбранные теги

            new_tags = form.cleaned_data["new_tags"]
            if new_tags:
                tag_names = [tag.strip() for tag in new_tags.split(",") if tag.strip()]
                for tag_name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    question.tags.add(tag)  # Добавляем новый тег к вопросу

            return redirect("question_list")
    else:
        form = QuestionForm(initial={"tags": selected_tags})
    return render(request, "add_question.html", {"form": form})


def edit_question(request, question_id):
    """Редактирование существующего вопроса"""
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("question_list")
    else:
        form = QuestionForm(instance=question)

    return render(request, "edit_question.html", {"form": form, "question": question})


def question_list(request):
    """Выводит список вопросов с фильтрацией по тегам"""
    tags_selected = request.GET.getlist("tags")
    questions = Question.objects.order_by("-created_at")

    if tags_selected:
        for tag_id in tags_selected:
            questions = questions.filter(tags__id=tag_id)

    tags = Tag.objects.all()

    return render(
        request,
        "question_list.html",
        {
            "questions": questions,
            "tags": tags,
            "tags_selected": list(map(int, tags_selected)),
        },
    )


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


def tag_list(request):
    """Список тегов"""
    tags = Tag.objects.all()
    return render(request, "tag_list.html", {"tags": tags})


def add_tag(request):
    """Создание нового тега"""
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
    else:
        form = TagForm()
    return render(request, "add_tag.html", {"form": form})


def edit_tag(request, tag_id):
    """Редактирование тега"""
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
    else:
        form = TagForm(instance=tag)
    return render(request, "edit_tag.html", {"form": form, "tag": tag})


def delete_tag(request, tag_id):
    """Удаление тега"""
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == "POST":
        tag.delete()
        return redirect("tag_list")
    return render(request, "delete_tag.html", {"tag": tag})
