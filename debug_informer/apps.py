import os
import socket
from datetime import (
    datetime,
    timezone,
)

from django.apps import AppConfig
from django.conf import settings
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
            'X-DI-Backend-Start-At': datetime.now(tz=timezone.utc).isoformat(),
        },
    }

    def ready(self):
        for k, v in self.get_defaults().items():
            setattr(self, k.upper(), self.get_setting(k, v))

    def get_defaults(self):
        return self.defaults.copy()

    def get_setting(self, key, default):
        key = f'{self.label.upper()}_{key.upper()}'
        return getattr(settings, key, default)
