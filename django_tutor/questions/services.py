from django_tutor.questions.models import Question, Tag
from django_tutor.questions.repositories import TagRepository


def get_sets_tags_by_parent_tags(selected_tags: list[str]) -> list[set[Tag]]:
    """Получаем множество дочерних тегов для каждого тега"""
    tags = Tag.objects.filter(id__in=selected_tags)

    return [TagRepository.get_descendant_tags(tag) for tag in tags]


def get_questions_by_tag_sets(tag_sets):
    if not tag_sets:
        return Question.objects.none()

    # TODO: это условие нужно переделать(по хорошему одним запросом)
    questions = set(
        Question.objects.filter(tags__in=tag_sets.pop()).prefetch_related("tags")
    )
    for tag_set in tag_sets:
        if tag_set:
            q = Question.objects.filter(tags__in=tag_set).prefetch_related("tags")
            questions.intersection(set(q))
    return questions
