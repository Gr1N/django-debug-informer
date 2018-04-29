# django-debug-informer [![Build Status](https://travis-ci.org/Gr1N/django-debug-informer.svg?branch=master)](https://travis-ci.org/Gr1N/django-debug-informer) [![codecov](https://codecov.io/gh/Gr1N/django-debug-informer/branch/master/graph/badge.svg)](https://codecov.io/gh/Gr1N/django-debug-informer) [![Updates](https://pyup.io/repos/github/Gr1N/django-debug-informer/shield.svg)](https://pyup.io/repos/github/Gr1N/django-debug-informer/)

The Django Debug Informer is a simple application that helps you to display various debug information about the Django project.

## Installation

    $ pip install django-debug-informer

And add `debug_informer` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = [
        # ...
        'debug_informer',
    ]

Add `DebugInformerHeadersMiddleware` to your `MIDDLEWARES` setting:

    MIDDLEWARES = [
        # ...
        'debug_informer.middleware.DebugInformerHeadersMiddleware',
    ]

Include the application urls into your project root urlconf:

    urlpatterns = [
        # ...
        path('djdi/', include('debug_informer.urls', namespace='djdi')),
    ]

Enjoy!

## Usage

To get Python version:

    $ http :8000/djdi/versions/python/
    HTTP/1.1 200 OK
    Content-Length: 132
    Content-Type: application/json
    Date: Sun, 29 Apr 2018 16:53:05 GMT
    Server: WSGIServer/0.2 CPython/3.6.5
    X-DI-Backend-Host: bat-book.local
    X-DI-Backend-Pid: 60817
    X-DI-Backend-Start-At: 2018-04-29T16:52:56.380979+00:00
    X-Frame-Options: SAMEORIGIN

    {
        "name": "Python",
        "version": "3.6.5 (default, Mar 30 2018, 06:41:53) \n[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)]"
    }

To get list of installed packages:

    ➔ http :8000/djdi/versions/packages/
    HTTP/1.1 200 OK
    Content-Length: 284
    Content-Type: application/json
    Date: Sun, 29 Apr 2018 16:54:52 GMT
    Server: WSGIServer/0.2 CPython/3.6.5
    X-DI-Backend-Host: bat-book.local
    X-DI-Backend-Pid: 60817
    X-DI-Backend-Start-At: 2018-04-29T16:52:56.380979+00:00
    X-Frame-Options: SAMEORIGIN

    {
        "list": [
            {
                "name": "wheel",
                "version": "0.31.0"
            },
            {
                "name": "setuptools",
                "version": "39.1.0"
            },
            {
                "name": "pytz",
                "version": "2018.4"
            },
            {
                "name": "pip",
                "version": "10.0.1"
            },
            {
                "name": "Django",
                "version": "2.0.4"
            },
            {
                "name": "django-debug-informer",
                "version": "0.3.1.dev0"
            }
        ],
        "total": 6
    }

To get specified package:

    $ http :8000/djdi/versions/packages/Django/
    HTTP/1.1 200 OK
    Content-Length: 38
    Content-Type: application/json
    Date: Sun, 29 Apr 2018 16:56:26 GMT
    Server: WSGIServer/0.2 CPython/3.6.5
    X-DI-Backend-Host: bat-book.local
    X-DI-Backend-Pid: 60817
    X-DI-Backend-Start-At: 2018-04-29T16:52:56.380979+00:00
    X-Frame-Options: SAMEORIGIN

    {
        "name": "Django",
        "version": "2.0.4"
    }

## Testing and linting

For testing and linting install [tox](http://tox.readthedocs.io):

    $ pip install tox

...and run:

    $ tox

## License

*django-debug-informer* is licensed under the MIT license. See the license file for details.
