#!/bin/bash
set -e

# Run migrations
echo "Running database migrations..."
cd luoibacstudio
uv run python manage.py migrate

# Create superuser if it doesn't exist (optional)
echo "Creating superuser..."
uv run python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser created: admin/admin')
else:
    print('Superuser already exists')
"

# Start the application
echo "Starting application..."
exec uv run gunicorn luoibacstudio.wsgi:application --bind 0.0.0.0:8000 --workers 3 