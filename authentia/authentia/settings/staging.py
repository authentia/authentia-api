from authentia.settings.base import *

DEBUG = False

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('AUTHENTIA_DB_NAME'),
        'USER': os.getenv('AUTHENTIA_DB_USER'),
        'PASSWORD': os.getenv('AUTHENTIA_DB_PASSWORD'),
        'HOST': os.getenv('AUTHENTIA_DB_HOST'),
        'PORT': os.getenv('AUTHENTIA_DB_PORT'),
    }
}
