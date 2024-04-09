from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST':os.environ.get('DATABASE_HOST'),
        'PORT':os.environ.get('DATABASE_PORT'),
    }
}

# After adding STATIC_ROOT run this command python manage.py collectstatic
# to copy admin static files into your project static dir
STATIC_ROOT = os.environ.get('STATIC_ROOT')
