# -*- coding: utf-8 -*-

import sys
from http import HTTPStatus

try:
    from pip.utils import get_installed_distributions
except ImportError:
    # Backward compatibility for pip<6.0.0
    from pip.util import get_installed_distributions

from django.http.response import JsonResponse
from django.views.generic import View

__all__ = (
    'IndexView',
    'VersionsPythonView',
    'VersionsPackagesView',
    'VersionsPackageView',
)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({})


class VersionsPythonView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'name': 'Python',
            'version': sys.version,
        })


class VersionsPackagesView(View):
    def get(self, request, *args, **kwargs):
        packages = [{
            'name': d.project_name,
            'version': d.version,
        } for d in get_installed_distributions()]

        return JsonResponse({
            'list': packages,
            'total': len(packages),
        })


class VersionsPackageView(View):
    def get(self, request, *args, **kwargs):
        packages = {
            d.project_name: d.version
            for d in get_installed_distributions()
        }
        package = kwargs['name']

        if package not in packages:
            return JsonResponse({}, status=HTTPStatus.NOT_FOUND.value)

        return JsonResponse({
            'name': package,
            'version': packages[package],
        })
