from django.urls import (
    include,
    path,
)

urlpatterns = [
    path('djdi/', include('debug_informer.urls', namespace='djdi')),
]
