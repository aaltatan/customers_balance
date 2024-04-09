from .base import *


DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [
  BASE_DIR / 'frontend' / 'public' / 'build'
] 