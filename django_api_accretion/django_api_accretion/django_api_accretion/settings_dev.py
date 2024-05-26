# settings for development environment
from .settings_base import * 
from dotenv import load_dotenv

# load .env configs
load_dotenv() 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('ENVIRONMENT') == 'development'

ALLOWED_HOSTS = []

# SQL lite database configuration 
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# PostGres database configuration 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "accretiondatabase"),
        'USER': os.getenv("DB_USER", os.getenv("DB_USER")),
        'PASSWORD': os.getenv("DB_PASSWORD", os.getenv("DB_PASSWORD")),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}