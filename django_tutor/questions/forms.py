from django import forms
from .models import Question, Answer, Tag


class QuestionForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )
    new_tags = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите новые теги через запятую",
            }
        ),
    )

    class Meta:
        model = Question
        fields = ["text", "source", "tags", "new_tags"]
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control",
                    "placeholder": "Введите ваш вопрос...",
                }
            ),
            "source": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Источник (книга, статья, ссылка)",
                }
            ),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text", "source", "confidence"]
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control",
                    "placeholder": "Введите ответ...",
                }
            ),
            "source": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Источник (книга, статья, ссылка)",
                }
            ),
            "confidence": forms.Select(attrs={"class": "form-control"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name", "parents"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Название тега"}
            ),
        }
        
    parents = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={"class": "form-control"})
    )
