# -*- coding: utf-8 -*-

import sys
from http import HTTPStatus

from django.core.urlresolvers import reverse_lazy, reverse
from django.test import TestCase


__all__ = (
    'IndexViewTests',
    'VersionsPythonViewTests',
    'VersionsPackagesViewTests',
    'VersionsPackageViewTests',
)


class IndexViewTests(TestCase):
    view_url = reverse_lazy('djdi:index')

    def test_ok(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class VersionsPythonViewTests(TestCase):
    view_url = reverse_lazy('djdi:versions:python')

    def test_ok(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        data = response.json()
        self.assertEqual(data['name'], 'Python')
        self.assertEqual(data['version'], sys.version)


class VersionsPackagesViewTests(TestCase):
    view_url = reverse_lazy('djdi:versions:packages')

    def test_ok(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        data = response.json()
        self.assertIn('total', data)

        for package in data['list']:
            self.assertIn('name', package)
            self.assertIn('version', package)


class VersionsPackageViewTests(TestCase):
    def view_url(self, name):
        return reverse('djdi:versions:package', args=(name,))

    def test_not_found(self):
        response = self.client.get(self.view_url('fakepackage'))
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_ok(self):
        response = self.client.get(self.view_url('Django'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

        data = response.json()
        self.assertEqual(data['name'], 'Django')
        self.assertIn('version', data)
