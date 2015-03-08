# -*- coding: utf-8 -*-

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module

from django.conf import settings

__all__ = (
    'PATCH_SETTINGS',

    'patch_all',
)


CONFIG_DEFAULTS = {

}

USER_CONFIG = getattr(settings, 'DEBUG_INFORMER_CONFIG', {})

CONFIG = CONFIG_DEFAULTS.copy()
CONFIG.update(USER_CONFIG)

PATCH_SETTINGS = getattr(
    settings, 'DEBUG_INFORMER_PATCH_SETTINGS', settings.DEBUG
)


def patch_all():
    patch_root_urlconf()


def patch_root_urlconf():
    from django.conf.urls import include, url
    from django.core.urlresolvers import clear_url_caches

    urlconf_module = import_module(settings.ROOT_URLCONF)
    urlconf_module.urlpatterns = [
        url(r'^djdi/', include('debug_informer.urls', namespace='djdi')),
    ] + urlconf_module.urlpatterns
    clear_url_caches()
