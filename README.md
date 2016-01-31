# django-debug-informer

[![Build Status](https://api.travis-ci.org/Gr1N/django-debug-informer.png "Build Status")](https://travis-ci.org/Gr1N/django-debug-informer)

The Django Debug Informer is a simple application that helps displays various debug information about the Django project. It works on Django 1.9.x and Python 3.5.x.


# Installation

Install the Debug Informer using [pip](http://www.pip-installer.org/):

    % pip install django-debug-informer

And add `debug_informer` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        'debug_informer',
    )

Add `DebugInformerHeadersMiddleware` to your `MIDDLEWARE_CLASSES` setting:

    MIDDLEWARE_CLASSES = [
        # ...
        'debug_informer.middleware.DebugInformerHeadersMiddleware',
    ]

Include the application urls into your project root urlconf:

    urlpatterns = [
        # ...
        url(r'^djdi/', include('debug_informer.urls', namespace='djdi')),
    ]

Enjoy!

# Usage

Get Python version:

    % curl -v http://127.0.0.1:8000/djdi/versions/python/
    ...
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < X-DI-Backend-Host: backend-host.local
    < X-DI-Backend-Pid: 11137
    < X-DI-Backend-Start-At: 2016-01-31T10:45:24.486301
    ...
    {
      "name": "Python",
      "version": "3.5.1 (default, Dec  7 2015, 21:59:10) \n[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.1.76)]"
    }

Get packages versions:

    % curl -v http://127.0.0.1:8000/djdi/versions/packages/
    ...
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < X-DI-Backend-Host: backend-host.local
    < X-DI-Backend-Pid: 11137
    < X-DI-Backend-Start-At: 2016-01-31T10:45:24.486301
    ...
    {
      "list": [
        {
          "name": "Django",
          "version": "1.9.1"
        },
        {
          "name": "pip",
          "version": "8.0.2"
        },
        {
          "name": "pluggy",
          "version": "0.3.1"
        },
        {
          "name": "py",
          "version": "1.4.31"
        },
        {
          "name": "setuptools",
          "version": "12.0.5"
        },
        {
          "name": "tox",
          "version": "2.3.1"
        },
        {
          "name": "virtualenv",
          "version": "14.0.3"
        }
      ],
      "total": 7
    }

Get version for package:

    % curl -v http://127.0.0.1:8000/djdi/versions/package/Django/
    ...
    < HTTP/1.0 200 OK
    < Content-Type: application/json
    < X-DI-Backend-Host: backend-host.local
    < X-DI-Backend-Pid: 11137
    < X-DI-Backend-Start-At: 2016-01-31T10:45:24.486301
    ...
    {
      "name": "Django",
      "version": "1.9.1"
    }

Specified package not found:

    % curl -v http://127.0.0.1:8000/djdi/versions/package/awesomepackage/
    ...
    < HTTP/1.0 404 NOT FOUND
    < Content-Type: application/json
    < X-DI-Backend-Host: backend-host.local
    < X-DI-Backend-Pid: 11137
    < X-DI-Backend-Start-At: 2016-01-31T10:45:24.486301
    ...
    {}


# License

*django-debug-informer* is licensed under the MIT license. See the license file for details.
