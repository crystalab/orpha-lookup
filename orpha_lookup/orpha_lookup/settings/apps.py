INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'django_object_actions',
    'rest_framework',
    'bulk_update_or_create',

    # Orpha apps
    'orpha_lookup.apps.data_parser',
    'orpha_lookup.apps.orpha',
]
