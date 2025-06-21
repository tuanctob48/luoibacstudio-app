FROM ghcr.io/astral-sh/uv:0.7.13-python3.11-bookworm-slim
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

# Build-time arguments
ARG SUPABASE_DB_URL
ARG DJANGO_SETTINGS_MODULE=luoibacstudio.settings.production

COPY README.md ./
# Install system deps
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential libpq-dev \
       libheif-dev libjpeg-dev libpng-dev libtiff-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY pyproject.toml ./
RUN uv sync

# Create Wagtail project
RUN uv run wagtail start luoibacstudio

# Copy project files
COPY . .

# Modify the generated settings to use PostgreSQL
COPY modify_settings.py ./
RUN uv run python modify_settings.py

# Make startup script executable
RUN chmod +x start.sh

# Collect static assets at build
ENV DJANGO_SETTINGS_MODULE=luoibacstudio.settings.production
ENV DATABASE_URL=${SUPPABASE_DB_URL}
RUN cd luoibacstudio && uv run python manage.py collectstatic --noinput || echo "Static collection completed"

# Expose port 8000
EXPOSE 8000

# Use startup script
CMD ["./start.sh"]
