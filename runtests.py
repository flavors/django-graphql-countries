#!/usr/bin/env python

import os
import sys

import django

from django.conf import settings
from django.test.runner import DiscoverRunner


DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=(
        'django_filters',
        'countries.apps.CountriesAppConfig',
        'tests'
    ),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['POSTGRES_DB_NAME'],
            'USER': os.environ.get('POSTGRES_DB_USER', 'postgres'),
            'PASSWORD': os.environ.get('POSTGRES_DB_PASSWORD', '')
        }
    }
)


def runtests():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    failures = DiscoverRunner(
        verbosity=1,
        interactive=True,
        failfast=False)\
        .run_tests(['tests'])

    sys.exit(failures)


if __name__ == '__main__':
    runtests()