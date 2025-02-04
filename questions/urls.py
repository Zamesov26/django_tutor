from django.urls import path
from .views import question_list, add_question

urlpatterns = [
    path("", question_list, name="question_list"),
    path("add/", add_question, name="add_question"),
]