from . import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False
ALLOWED_HOSTS = ['161.35.56.191']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'purbeurre', # le nom de notre base de données créée précédemment
        'USER': 'fp', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'megamotdepasse',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

sentry_sdk.init(
    dsn="https://b034650fac4846809cb320efa07cc7e2@o402720.ingest.sentry.io/5265819",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
