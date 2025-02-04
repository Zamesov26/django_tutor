import os

from celery import shared_task
from celery.exceptions import MaxRetriesExceededError


@shared_task(rate_limit="10/m")
def play_sound_task(iteration=1, max_iterations=3):
    """Воспроизводит звуковой сигнал и автоматически перезапускает себя 3 раза"""
    try:
        print("🔊 Воспроизвожу сигнал...")
        os.system("paplay /usr/share/sounds/freedesktop/stereo/message.oga")  # Воспроизводит звук в Ubuntu
        raise ValueError
    except Exception as e:
        try:
            if iteration < max_iterations:
                play_sound_task.apply_async(args=[iteration + 1, max_iterations], countdown=5)
        except MaxRetriesExceededError:
            print("⚠️ Достигнуто максимальное количество повторов!")
    
    return "✅ Завершено!"
