from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text", "source"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 3, "class": "form-control", "placeholder": "Введите ваш вопрос..."}),
            "source": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Источник (книга, статья, ссылка)"}
            ),

        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text", "source", "confidence"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 3, "class": "form-control", "placeholder": "Введите ответ..."}),
            "source": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Источник (книга, статья, ссылка)"}
            ),
            "confidence": forms.Select(attrs={"class": "form-control"}),
        }