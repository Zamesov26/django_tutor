from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(
        "Название", max_length=50, unique=True, db_index=True
    )
    parents = models.ManyToManyField(
        "self", blank=True, related_name="children", symmetrical=False
    )

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField("Текст вопроса")
    source = models.CharField("Источник", max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="questions")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.text[:50]


class Answer(models.Model):
    CONFIDENCE_LEVELS = [
        (1, "Низкая"),
        (2, "Средняя"),
        (3, "Высокая"),
    ]

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    text = models.TextField("Текст ответа", blank=True, null=True)
    source = models.CharField("Источник", max_length=128, blank=True, null=True)
    confidence = models.IntegerField(
        "Уверенность", choices=CONFIDENCE_LEVELS, default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")  # Автор ответа

    def __str__(self):
        return f"Ответ на: {self.question.text[:30]}"
