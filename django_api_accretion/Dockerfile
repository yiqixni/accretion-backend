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
    rm -rf /var/lib/apt/lists/* 

## install python packages ##
RUN pip install --upgrade pip && pip install -r requirements.txt 

# Create shared group and add users
RUN groupadd -r webgroup && \
    useradd -r -g webgroup django && \
    usermod -aG webgroup www-data

## create static file directory and grant permission ##
RUN mkdir -p                    /vol/web/static /vol/web/media && \
    # change ownership from root to django user
    chown -R django:webgroup    /django_api_accretion /vol /vol/web/static /vol/web/media && \
    # allow the owner to write/read
    chmod -R 775                /vol /vol/web/static /vol/web/media && \    
    chmod -R 775                /django_api_accretion 

## change user to django instead of default root user 
USER django

# Copy entrypoint script
COPY ./scripts/entrypoint.sh /entrypoint.sh

# Ensure the entrypoint script is executable
# RUN chmod +x /entrypoint.sh

# Expose the port the app runs on
# EXPOSE 8000

VOLUME /vol/web/static /vol/web/media

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]