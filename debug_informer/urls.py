from django.urls import (
    include,
    path,
)

from debug_informer.views import (
    IndexView,
    VersionsPackagesView,
    VersionsPackageView,
    VersionsPythonView,
)

app_name = 'debug_informer'

versions_patterns = ([
    path('python/', VersionsPythonView.as_view(), name='python'),
    path('packages/', VersionsPackagesView.as_view(), name='packages'),
    path('packages/<slug:name>/', VersionsPackageView.as_view(), name='package'),
], 'versions')

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('versions/', include(versions_patterns, namespace='versions')),
]
