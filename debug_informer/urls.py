# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from debug_informer.views import (
    IndexView,
    VersionsPythonView,
    VersionsPackagesView,
    VersionsPackageView,
)


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^versions/', include([
        url(r'^python/$', VersionsPythonView.as_view(), name='python'),
        url(r'^packages/$', VersionsPackagesView.as_view(), name='packages'),
        url(r'^package/(?P<name>[a-zA-Z0-9_-]+)/$',
            VersionsPackageView.as_view(), name='package'),
    ], namespace='versions')),
]
