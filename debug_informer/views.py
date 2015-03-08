# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.views.generic import View
from django.utils.six import iteritems
from django.utils.six.moves import http_client

from debug_informer.logic import (
    Versions,
)

__all__ = (
    'IndexView',
    'VersionsView',
)


CONTENT_TYPE_JSONAPI = 'application/vnd.api+json'


class BaseView(View):
    view_name = None

    def jsonapi_response(self, data=None, status=http_client.OK):
        # http://jsonapi.org/format/

        content = {
            'links': {
                'self': self.request.get_full_path(),
            },
            'data': data,
        }
        content = json.dumps(content, indent=2)

        return HttpResponse(content=content, content_type=CONTENT_TYPE_JSONAPI,
                            status=status)

    def not_found_response(self):
        return HttpResponse(status=http_client.NOT_FOUND)


class IndexView(BaseView):
    view_name = 'djdi:index'

    def get(self, request, *args, **kwargs):
        return self.jsonapi_response()


class VersionsView(BaseView):
    view_name = 'djdi:versions'

    categories = (
        'python',
        'packages',
    )

    def get(self, request, *args, **kwargs):
        category = kwargs['category']

        return getattr(self, 'handle_{0}'.format(category))(
            request, *args, **kwargs
        )

    def handle_python(self, request, *args, **kwargs):
        return self.jsonapi_response(data={
            'category': 'python',
            'version': Versions.python(),
        })

    def handle_packages(self, request, *args, **kwargs):
        packages = Versions.packages()
        package_name = kwargs['name']

        if package_name:
            return self.handle_package(packages, package_name)

        data = [{
            'category': 'packages',
            'name': name,
            'version': version,
        } for name, version in iteritems(packages)]

        return self.jsonapi_response(data=data)

    def handle_package(self, packages, name):
        if name not in packages:
            return self.not_found_response()

        return self.jsonapi_response(data={
            'category': 'packages',
            'name': name,
            'version': packages[name],
        })
