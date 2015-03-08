# -*- coding: utf-8 -*-

import sys

try:
    from pip.utils import get_installed_distributions
except ImportError:
    # Backward compatibility for pip<6.0.0
    from pip.util import get_installed_distributions

__all__ = (
    'Versions',
)


class Versions(object):
    @classmethod
    def python(cls):
        return sys.version

    @classmethod
    def packages(cls):
        return dict(
            # TODO: return location for editable distributions
            (d.project_name, d.version,)
            for d in get_installed_distributions()
        )
