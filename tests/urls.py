from django.urls import path, include


urlpatterns = [
    path('__tests/djdi/', include('debug_informer.urls', namespace='djdi')),
]
