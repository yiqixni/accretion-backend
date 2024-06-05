# Use the official Python image from the Docker Hub
FROM python:3.10.14-slim

LABEL maintainer="accretion.life" 

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /django_api_accretion

## Install dependencies using requirements.txt ##
COPY requirements.txt /django_api_accretion/requirements.txt

# Copy the application code to the working directory
COPY ./django_api_accretion /django_api_accretion/

## Install system dependencies  ##
RUN apt-get update && \
    apt-get install -y --no-install-recommends  \
            build-essential  \
            libpq-dev  \
            gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \ 
    pip install --upgrade pip && pip install -r requirements.txt && \
    # create django as non-root user
    adduser --disabled-password --no-create-home django  && \
    # create static file directory and grant permission 
    mkdir -p /vol/web/static /vol/web/media && \
    chmod -R 755 /vol && \    
    # create socket directory and grant permission 
    mkdir -p /django_api_accretion/sockets && \ 
    chmod -R 755 /django_api_accretion && \
    # change ownership from root to django user
    chown -R django /django_api_accretion /vol

## change user to django instead of default root user 
USER django

# Copy entrypoint script
COPY ./scripts/entrypoint.sh /entrypoint.sh

# Ensure the entrypoint script is executable
# RUN chmod +x /entrypoint.sh

# Expose the port the app runs on
# EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Run the application: commented out run gunicorn in docker-compose 
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_api_accretion.wsgi:application"]