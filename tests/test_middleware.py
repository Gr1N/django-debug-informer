from http import HTTPStatus

from django.apps import apps as djapps
from django.test import TestCase
from django.urls import reverse_lazy

settings = djapps.get_app_config('debug_informer')

__all__ = (
    'DebugInformerHeadersMiddlewareTests',
)


class DebugInformerHeadersMiddlewareTests(TestCase):
    view_url = reverse_lazy('djdi:index')

    def test__ok(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        for key, value in settings.HEADERS.items():
            self.assertEqual(response[key], str(value))
