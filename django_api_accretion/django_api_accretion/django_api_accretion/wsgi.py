"""
WSGI config for django_api_accretion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_api_accretion.settings_dev")

if os.getenv('ENVIRONMENT') == 'production':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_api_accretion.settings_prod'


application = get_wsgi_application()
