from django.db import models

class Question(models.Model):
    text = models.TextField("Текст вопроса")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]