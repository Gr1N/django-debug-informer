# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from debug_informer.views import (
    IndexView,
    VersionsView,
)


urlpatterns = patterns('',
    url(r'^$',
        IndexView.as_view(), name='index'),
    url(r'^versions/(?P<category>%(categories)s)/(?P<name>[a-zA-Z0-9_-]+)?/?$' % {'categories': '|'.join(VersionsView.categories)},
        VersionsView.as_view(), name='versions'),
)
