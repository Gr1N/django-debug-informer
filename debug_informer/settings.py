# -*- coding: utf-8 -*-

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module

from django.conf import settings

__all__ = (
    'PATCH_SETTINGS',
)


CONFIG_DEFAULTS = {

}

USER_CONFIG = getattr(settings, 'DEBUG_INFORMER_CONFIG', {})

CONFIG = CONFIG_DEFAULTS.copy()
CONFIG.update(USER_CONFIG)

PATCH_SETTINGS = getattr(
    settings, 'DEBUG_INFORMER_PATCH_SETTINGS', settings.DEBUG
)
