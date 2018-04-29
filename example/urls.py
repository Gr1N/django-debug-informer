from django.conf.urls import include, url


urlpatterns = [
    url(r'^djdi/', include('debug_informer.urls', namespace='djdi')),
]
