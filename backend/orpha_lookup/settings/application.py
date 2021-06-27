import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

XML_FILE_URL = 'http://www.orphadata.org/data/xml/en_product4.xml'
XML_UPLOAD_PATH = os.path.join(BASE_DIR, 'var', 'data.xml')

# Django-specific
ROOT_URLCONF = 'orpha_lookup.urls'
WSGI_APPLICATION = 'orpha_lookup.wsgi.application'
SECRET_KEY = 'django-insecure-$$x@ik#sz!1&!sax9@^syxl9-lf(0mwrkbv7h4#lmqs(+t(#=6'
DEBUG = True
ALLOWED_HOSTS = []
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
