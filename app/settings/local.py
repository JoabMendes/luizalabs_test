
from app.settings.base import *
from django.conf import settings
from django.conf.urls.static import static

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# Uses SQLite3 for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local_database.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# add static root to properly configure collectstatic under local dev
urlpatterns = [] + static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)