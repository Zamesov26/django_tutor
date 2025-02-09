from django.db import models

from .models import Tag, Question

class TagRepository:
    @staticmethod
    def get_descendant_tags(tag: Tag) -> set[Tag]:
        """Рекурсивно получаем все дочерние теги"""
        children = Tag.objects.filter(parents=tag)
        if not children:
            return {tag}
        
        descendants = set(children)
        for child in children:
            if child:
                descendants.add(tag)
                descendants.update((TagRepository.get_descendant_tags(child) | {child}))
        return descendants

class QuestionRepository:
    @staticmethod
    def get_questions_by_tags(tags):
        """Получаем вопросы, у которых есть все указанные теги"""
        return (
            Question.objects
            .filter(tags__in=tags)
            .annotate(tag_count=models.Count("tags"))
            .filter(tag_count=len(tags))  # Оставляем только вопросы, у которых есть все переданные теги
        )