import sys
from http import HTTPStatus

from django.http import JsonResponse
from django.views import View
from pip._internal.utils.misc import get_installed_distributions

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
