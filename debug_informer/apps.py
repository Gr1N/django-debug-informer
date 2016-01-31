# -*- coding: utf-8 -*-

import os
import socket
from datetime import datetime

from django.conf import settings

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'Config',
)


class Config(AppConfig):
    name = 'debug_informer'
    verbose_name = _('Django Debug Informer')

    defaults = {
        'headers': {
            'X-DI-Backend-Host': socket.gethostname(),
            'X-DI-Backend-Pid': os.getpid(),
            'X-DI-Backend-Start-At': datetime.utcnow().isoformat(),
        },
    }

    def ready(self):
        for k, v in self.get_defaults().items():
            setattr(self, k.upper(), self.get_setting(k, v))

    def get_defaults(self):
        return self.defaults.copy()

    def get_setting(self, key, default):
        return getattr(settings, '{0}_{1}'.format(
            self.label.upper(),
            key.upper()
        ), default)
