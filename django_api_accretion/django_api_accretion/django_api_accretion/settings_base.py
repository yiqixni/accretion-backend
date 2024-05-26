from pathlib import Path
from datetime import timedelta
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    "buy",
    "sell",
    "contact", 
    "database", 
    "database_visualization",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework", 
    "debug_toolbar", 
    "corsheaders", 
    "rest_framework.authtoken",    
    "djoser", # Djoser authentication
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware", 
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "django_api_accretion.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_api_accretion.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer', 
        'rest_framework.renderers.BrowsableAPIRenderer', 
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [        
        'rest_framework_simplejwt.authentication.JWTAuthentication', # simpleJWT authentication        
        'rest_framework.authentication.TokenAuthentication', # DRF token authentication
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_THROUTTLE_RATES': {
        'anon': '1/day',
        'user': '1/day',
    },
    'DEFAULT_THROUTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle', 
    ],
}

# used for debugging toolbar
INTERNAL_IPS = [
    "127.0.0.1", 
]

# Configure corsheaders
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", 
    "https://accretion.life",
    "https://www.accretion.life",  
    "https://4f4c-2607-fb90-9e17-4939-1069-14dd-683-ed6e.ngrok-free.app",    
]

CORS_ALLOWED_METHODS = [
    "GET", 
    "POST", 
    "PUT", 
    "PATCH", 
    "DELETE", 
    "OPTIONS", 
]

# leave allowed headers empty => allow default headers 
CORS_ALLOWED_HEADERS = [
    
]

# UPLOADED FILES CONFIGURATION
MEDIA_URL = "/media/" 
MEDIA_ROOT = os.path.join(BASE_DIR, "media") 

# Configure Djoser
DJOSER = {
    "USER_ID_FIELD": "username", 
    "LOGIN_FIELD": "username", #"email", 
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SERIALIZERS": {        
        "user_create": "djoser.serializers.UserCreateSerializer", ## Djoser default account serializer 
    }, 
}

# Configure JWT 
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30), 
}

# Django Email backend setup using django-ses library
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_SES_REGION_NAME = 'us-east-2'  # e.g., 'us-east-1'
# Optional: If you want to use a specific SES verified email address as the sender
DEFAULT_FROM_EMAIL = 'yiqinix@gmail.com'
# SERVER_EMAIL = 'support@accretion.life'

