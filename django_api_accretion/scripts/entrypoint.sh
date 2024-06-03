#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files (if necessary)
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# Start server
echo "Starting server..."
exec "$@"
