# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'Config',
)


class Config(AppConfig):
    name = 'debug_informer'
    verbose_name = _('Django Debug Informer')
