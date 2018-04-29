from django.urls import (
    include,
    path,
)

urlpatterns = [
    path('__tests/djdi/', include('debug_informer.urls', namespace='djdi')),
]
