# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from debug_informer import settings as di_settings

__all__ = (
    'DebugInformerConfig',
)


class DebugInformerConfig(AppConfig):
    name = 'debug_informer'
    verbose_name = _('Debug Informer')

    def ready(self):
        if not di_settings.PATCH_SETTINGS:
            return

        di_settings.patch_all()
