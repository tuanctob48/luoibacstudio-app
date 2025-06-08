FROM python:3.11-slim
WORKDIR /app

# Install system deps
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt gunicorn

# Copy project
COPY . .

# Collect static assets at build
ENV DJANGO_SETTINGS_MODULE=luoibac.studio.settings.production
ENV DATABASE_URL=${POSTGRES_URL}
RUN python manage.py collectstatic --noinput

# Use Gunicorn
CMD ["gunicorn", "luoibac.studio.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
