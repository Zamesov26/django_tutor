import os
from celery import Celery

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "django_tutor.settings"
)  # Замени myproject на имя своего проекта

celery_app = Celery("django_tutor")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
