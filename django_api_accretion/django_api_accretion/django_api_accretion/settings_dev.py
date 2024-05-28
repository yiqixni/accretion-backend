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

#### STATIC/MEDIA FILE CONFIGURATION ####
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# UPLOADED FILES CONFIGURATION
MEDIA_URL = "/media/" 
MEDIA_ROOT = os.path.join(BASE_DIR, "media") 


# # SQL lite database configuration # Deprecated # 
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
        'NAME': os.getenv("DB_NAME", os.getenv("DB_NAME")),
        'USER': os.getenv("DB_USER", os.getenv("DB_USER")),
        'PASSWORD': os.getenv("DB_PASSWORD", os.getenv("DB_PASSWORD")),        
        'HOST': os.getenv("DB_HOST", os.getenv("DB_HOST")), # for Docker container        
        'PORT': os.getenv("DB_PORT", os.getenv("DB_PORT")),
        # 'NAME': os.getenv("DB_NAME", "accretiondatabase"),
        # 'HOST': "localhost", # for running backend without Docker         
        # 'HOST': os.getenv("DB_HOST", "db"),
        # 'PORT': os.getenv("DB_PORT", "5432"),        
    }
}