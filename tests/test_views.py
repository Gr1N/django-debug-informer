# -*- coding: utf-8 -*-

import json
import sys

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.six.moves import http_client

from debug_informer.views import (
    IndexView,
    VersionsView,
)

__all__ = (
    'IndexViewTests',
    'VersionsViewTests',
)


class IndexViewTests(TestCase):
    def view_url(self):
        return reverse(IndexView.view_name)

    def test_post_not_allowed(self):
        response = self.client.post(self.view_url())
        self.assertEqual(response.status_code, http_client.METHOD_NOT_ALLOWED)

    def test_get_ok(self):
        response = self.client.get(self.view_url())
        self.assertEqual(response.status_code, http_client.OK)


class VersionsViewTests(TestCase):
    def view_url(self, category, name=None):
        args = (category,)
        if name is not None:
            args = args + (name,)

        return reverse(VersionsView.view_name, args=args)

    def test_post_not_allowed(self):
        response = self.client.post(self.view_url('python'))
        self.assertEqual(response.status_code, http_client.METHOD_NOT_ALLOWED)

    def test_python(self):
        response = self.client.get(self.view_url('python'))
        self.assertEqual(response.status_code, http_client.OK)

        content = json.loads(response.content.decode('utf-8'))
        data = content['data']
        self.assertEqual(data['category'], 'python')
        self.assertEqual(data['version'], sys.version)

    def test_packages(self):
        response = self.client.get(self.view_url('packages'))
        self.assertEqual(response.status_code, http_client.OK)

        content = json.loads(response.content.decode('utf-8'))
        data = content['data']
        for package in data:
            self.assertEqual(package['category'], 'packages')
            self.assertIn('name', package)
            self.assertIn('version', package)

    def test_package(self):
        response = self.client.get(self.view_url('packages', name='Django'))
        self.assertEqual(response.status_code, http_client.OK)

        content = json.loads(response.content.decode('utf-8'))
        data = content['data']
        self.assertEqual(data['category'], 'packages')
        self.assertEqual(data['name'], 'Django')

    def test_package_not_found(self):
        response = self.client.get(self.view_url(
            'packages', name='fakepackage'
        ))
        self.assertEqual(response.status_code, http_client.NOT_FOUND)
