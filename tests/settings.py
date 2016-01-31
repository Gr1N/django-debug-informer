# -*- coding: utf-8 -*-
"""
Django settings for tests.
Quick-start development settings - unsuitable for production.
"""

import os

import django


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_informer',
    'tests',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_informer.middleware.DebugInformerHeadersMiddleware',
]

ROOT_URLCONF = 'tests.urls'


if django.VERSION[:2] < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
