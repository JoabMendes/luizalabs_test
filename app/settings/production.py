
from app.settings.base import *
import dj_database_url

DEBUG = False
# Admins (For sending erros log)
ADMINS = [('Joab Mendes', 'joab.mendes.r2d2@gmail.com')]

if bool(os.getenv('HEROKU_ENV', False)):
    # If it's hereku just use the url
    DATABASES['default'] = dj_database_url.config()
else:
    # Makes configuration for other servers
    # postgres config for django
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }