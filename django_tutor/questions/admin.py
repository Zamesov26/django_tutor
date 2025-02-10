from django.contrib import admin

from .models import Answer, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "source", "created_at")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "text", "source", "confidence", "created_at")
