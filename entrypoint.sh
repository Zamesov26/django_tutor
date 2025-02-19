#!/bin/sh

echo "Waiting for database to be ready..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database is ready!"

echo "Applying database migrations..."
python manage.py migrate

echo "Starting Django server..."
exec "$@"
