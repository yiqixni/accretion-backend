# settings for development environment
import os 
from .settings_base import * 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
print(f"=====Starting Django in {os.getenv('ENVIRONMENT')} environment====")

ALLOWED_HOSTS = []

#### STATIC/MEDIA FILE CONFIGURATION ####
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

# UPLOADED FILES CONFIGURATION
MEDIA_URL = "/media/" 
# MEDIA_ROOT = os.path.join(BASE_DIR, "media") 

## static root for Docker 
MEDIA_ROOT = "/vol/web/media"
STATIC_ROOT = "/vol/web/static"

## PostGres database configuration 
## docker-compose.yml get environment from .env and defines the environment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',        
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),        
        'HOST': os.getenv("DB_HOST"),         
        'PORT': os.getenv("DB_PORT"),    
    }
}