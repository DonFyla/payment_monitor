#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if credentials provided..."
python manage.py create_superuser

echo "Starting Gunicorn..."
exec gunicorn chess_academy.wsgi:application --bind 0.0.0.0:$PORT --workers 4 --threads 2
