# -*- coding: utf-8 -*-

from http import HTTPStatus

from django.apps import apps as djapps
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase

settings = djapps.get_app_config('debug_informer')

__all__ = (
    'DebugInformerHeadersMiddlewareTests',
)


class DebugInformerHeadersMiddlewareTests(TestCase):
    view_url = reverse_lazy('djdi:index')

    def test_ok(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        for key, value in settings.HEADERS.items():
            self.assertEqual(response[key], str(value))
