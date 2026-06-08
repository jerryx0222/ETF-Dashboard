FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 安裝 MySQL 編譯所需的底層套件
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 🔥 修正 A：因為 Dockerfile 在根目錄，必須指定去 backend 資料夾拿 requirements.txt
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 🔥 修正 B：將本地 backend 資料夾內的所有 Django 程式碼，複製到容器的 /app 中
COPY backend/ .

# GCP Cloud Run 不需要 EXPOSE 8000，它會忽略這個設定，可以放著或不寫

# 🔥 修正 C：GCP 要求必須綁定系統環境變數 $PORT，不能寫死 0.0.0.0:8000
# 同時加上 --timeout 0 來配合 Cloud Run 的連線特性
CMD exec gunicorn config.wsgi:application --bind :$PORT --workers 1 --threads 8 --timeout 0