#!/bin/sh

echo "Waiting for database to be ready..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database is ready!"

echo "Applying database migrations..."
python manage.py migrate

# Создаем суперпользователя, если он не существует
echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.getenv("DJANGO_SUPERUSER_USERNAME")
email = os.getenv("DJANGO_SUPERUSER_EMAIL")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created!")
else:
    print("Superuser already exists.")
EOF

echo "Starting Django server..."
exec "$@"
