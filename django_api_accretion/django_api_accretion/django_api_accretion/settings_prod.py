# settings_prod.py for the production environment 
import os 
from .settings_base import *

DEBUG = True

print(f"=====Starting Django in {os.getenv('ENVIRONMENT')} environment====")

#define allowed host like accretion.life
ALLOWED_HOSTS = [
    "backend-1.accretion.life", 
    "http://127.0.0.1", # for local testing 
    "localhost", 
    "http://3.147.46.192", # for EC2 instance 
    "unix:/django_api_accretion/django_api_accretion/app.sock", # for unix socket connection
] 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

#### STATIC/MEDIA FILE CONFIGURATION ####

# UPLOADED FILES CONFIGURATION
STATIC_URL = "/static/"
MEDIA_URL = "/media/" 

## static root for Docker 
MEDIA_ROOT = "/vol/web/media"
STATIC_ROOT = "/vol/web/static"


## Configuration for storing static files on AWS S3 ##

# # AWS S3 Configuration
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }

# # Static files (CSS, JavaScript, images)
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 

# # Media files
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # Security settings
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# X_FRAME_OPTIONS = 'DENY'
