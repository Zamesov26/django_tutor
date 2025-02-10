from django.urls import path

from .views import (
    add_answer,
    add_question,
    add_tag,
    delete_tag,
    edit_question,
    edit_tag,
    question_detail,
    question_list,
    tag_list,
)

urlpatterns = [
    path("", question_list, name="question_list"),
    path("add/", add_question, name="add_question"),
    path("<int:question_id>/", question_detail, name="question_detail"),
    path("<int:question_id>/add-answer/", add_answer, name="add_answer"),
    path("tags/", tag_list, name="tag_list"),
    path("tags/add/", add_tag, name="add_tag"),
    path("tags/<int:tag_id>/edit/", edit_tag, name="edit_tag"),
    path("tags/<int:tag_id>/delete/", delete_tag, name="delete_tag"),
    path("questions/<int:question_id>/edit/", edit_question, name="edit_question"),
]
