from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 3, "class": "form-control", "placeholder": "Введите ваш вопрос..."})
        }
