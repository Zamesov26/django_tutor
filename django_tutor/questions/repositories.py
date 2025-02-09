from .models import Tag


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