# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libpq-dev \
       gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv and compile requirements
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system --deploy

# Copy the application code to the working directory
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_api_accretion.wsgi:application"]
