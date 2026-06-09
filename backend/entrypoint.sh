#!/bin/sh
set -e

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Starting server..."
exec gunicorn config.wsgi:application --bind :${PORT:-8080} --workers 1 --threads 8 --timeout 0
