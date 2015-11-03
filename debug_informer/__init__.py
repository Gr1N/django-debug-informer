# -*- coding: utf-8 -*-

__all__ = (
    'VERSION',
)


try:
    import pkg_resources
    VERSION = pkg_resources.get_distribution('django-debug-informer').version
except Exception:
    VERSION = 'unknown'
