# NOTE: This is all boilerplate, don't edit this file!! (Still run it, however)
import sys
import os
from django.conf import settings
from django.core.management import execute_from_command_line


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    ROOT_URLCONF='urls',
    STATIC_URL='static/',
    STATIC_ROOT=os.path.join(BASE_DIR, 'static'),
    INSTALLED_APPS=[
        'django.contrib.staticfiles',
    ],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }],
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
    EMAIL_USE_TLS=False,
    EMAIL_HOST='mail.kevindublin.com',
    EMAIL_PORT=587,
    EMAIL_HOST_USER='vin@kevindublin.com',
    EMAIL_HOST_PASSWORD='##One4rt##',
)

execute_from_command_line(sys.argv)
