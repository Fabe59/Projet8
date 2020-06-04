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
    dsn="https://f335ae6a40c24808aa5137fe6f6013a2@o402720.ingest.sentry.io/5264251",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
<<<<<<< HEAD
)
=======
)
>>>>>>> 1a5e1e85d9074e4dc929d5a0678e5c1cd75232b3
