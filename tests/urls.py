# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
    url(r'^__tests/djdi/', include('debug_informer.urls', namespace='djdi')),
)
