from django.urls import path
from .views import question_list, question_detail, add_answer, add_question, send_sound

urlpatterns = [
    path("", question_list, name="question_list"),  # Показываем только список вопросов
    path("add/", add_question, name="add_question"),  # Добавление вопроса
    path(
        "<int:question_id>/", question_detail, name="question_detail"
    ),  # Просмотр вопроса и ответов
    path(
        "<int:question_id>/add-answer/", add_answer, name="add_answer"
    ),  # Форма для добавления ответа
    path("<int:question_id>/send/", send_sound, name="send_sound"),
]
