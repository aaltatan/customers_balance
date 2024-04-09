from .base import *
from dotenv import load_dotenv

load_dotenv(BASE_DIR)

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [
  BASE_DIR / 'frontend' / 'public' / 'build'
] 