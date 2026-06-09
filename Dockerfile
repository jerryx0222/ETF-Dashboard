# Stage 1: Build React frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /frontend
COPY frontend/package.json .
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Django backend
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .
COPY --from=frontend-builder /frontend/build /app/frontend_build

# collectstatic is DB-free; dummy SECRET_KEY satisfies Django startup check
RUN SECRET_KEY=build-time-dummy python manage.py collectstatic --noinput

CMD exec gunicorn config.wsgi:application --bind :${PORT:-8080} --workers 1 --threads 8 --timeout 0
