FROM python:3.10.5


ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    python3-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN cp -n ../.env.example .env || true

COPY .env .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirement.txt

RUN echo '#!/bin/bash\n\
# Wait for the database to be ready\n\
sleep 10\n\
# Apply migrations\n\
python manage.py makemigrations\n\
python manage.py migrate\n\
# Start the server\n\
python manage.py runserver 0.0.0.0:8000\n'\
> /app/start.sh && chmod +x /app/start.sh

EXPOSE 8000

CMD ["/app/start.sh"]