from django.apps import apps as djapps

settings = djapps.get_app_config('debug_informer')

__all__ = (
    'DebugInformerHeadersMiddleware',
)


class DebugInformerHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        headers = getattr(settings, 'HEADERS', {})
        for key, value in headers.items():
            response[key] = value

        return response
