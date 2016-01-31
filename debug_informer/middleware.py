# -*- coding: utf-8 -*-

from django.apps import apps as djapps

settings = djapps.get_app_config('debug_informer')

__all__ = (
    'DebugInformerHeadersMiddleware',
)


class DebugInformerHeadersMiddleware(object):
    def process_response(self, request, response):
        headers = getattr(settings, 'HEADERS', {})
        for key, value in headers.items():
            response[key] = value

        return response
