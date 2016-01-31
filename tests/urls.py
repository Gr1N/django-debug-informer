# -*- coding: utf-8 -*-

from django.conf.urls import include, url


urlpatterns = [
    url(r'^__tests/djdi/', include('debug_informer.urls', namespace='djdi')),
]
