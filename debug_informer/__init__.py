# -*- coding: utf-8 -*-

__all__ = (
    'VERSION',

    'default_app_config',
)


try:
    import pkg_resources
    VERSION = pkg_resources.get_distribution('django-debug-informer').version
except Exception:
    VERSION = 'unknown'


default_app_config = 'debug_informer.apps.DebugInformerConfig'
