import os

from .base import *  
from .utils import strtobool

DEBUG = strtobool(os.getenv("DEBUG", "y"))

CORS_ALLOW_ALL_ORIGINS = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}