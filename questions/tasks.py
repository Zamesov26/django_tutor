import functools
import os
from random import randint

from celery import shared_task, current_task
from django.db import models

from questions.models import Question


def retry_on_failure(model):
    """
    Декоратор, который увеличивает счетчик попыток в базе данных по `id` в случае возникновения исключений.
    
    Аргументы:
        model (models.Model): Django-модель, в которой нужно увеличивать `attempts`
    """
    
    def decorator(func):
        """Декоратор для логирования вызова задачи"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            id_ = kwargs.get("id", args[0] if args else None)
            if id_ is None:
                raise ValueError(
                    "❌ Ошибка: id должен быть передан как именованный аргумент (id=...) или первым позиционным."
                )
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                model.objects.filter(id=id_).update(attempts=models.F("attempts") + 1)
                raise
            return res
        return wrapper
    
    return decorator

@shared_task(name="play_sound_task", acks_late=True)
@retry_on_failure(model=Question)
# @transaction.atomic
def play_sound_task(id_):
    os.system("paplay /usr/share/sounds/freedesktop/stereo/message.oga")  # Воспроизводит звук в Ubuntu
    n = randint(1, 2)
    # if n == 1:
    current_task.apply_async(args=[id_], countdown=5)
    # raise ValueError
    # """Воспроизводит звуковой сигнал и автоматически перезапускает себя 3 раза"""
    # print(f"🔊 Воспроизвожу сигнал...{id_} {iteration} {max_iterations}")
    #
    # if iteration < max_iterations:
    #     play_sound_task.apply_async(args=[id_, iteration + 1, max_iterations], countdown=5)
    # else:
    #     print("⚠️ Достигнуто максимальное количество повторов!")
    #     # raise MaxRetriesExceededError
    
    # return "✅ Завершено!"
