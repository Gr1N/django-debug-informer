# django-debug-informer

[![Build Status](https://api.travis-ci.org/Gr1N/django-debug-informer.png "Build Status")](https://travis-ci.org/Gr1N/django-debug-informer)

The Django Debug Informer is a simple application that helps displays various debug information about the Django project. It works on Django 1.4.x to 1.7.x and Python 2.6.x to 3.4.x.


# Installation

Install the Debug Informer using [pip](http://www.pip-installer.org/):

    % pip install django-debug-informer

And add `debug_informer` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        'debug_informer',
    )

Enjoy!

# Usage

Get Python version:

    % curl -v http://127.0.0.1:8000/djdi/versions/python/
    ...
    < HTTP/1.0 200 OK
    < Content-Type: application/vnd.api+json
    ...
    {
      "data": {
        "category": "python",
        "version": "2.7.6 (default, Sep  9 2014, 15:04:36) \n[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)]"
      },
      "links": {
        "self": "/djdi/versions/python/"
      }
    }

Get packages versions:

    % curl -v http://127.0.0.1:8000/djdi/versions/packages/
    ...
    < HTTP/1.0 200 OK
    < Content-Type: application/vnd.api+json
    ...
    {
      "data": [
        {
          "category": "packages",
          "version": "3.7.1",
          "name": "coverage"
        },
        {
          "category": "packages",
          "version": "1.7.5",
          "name": "Django"
        },
        {
          "category": "packages",
          "version": "12.0.5",
          "name": "setuptools"
        },
        {
          "category": "packages",
          "version": "6.0.8",
          "name": "pip"
        }
      ],
      "links": {
        "self": "/djdi/versions/packages/"
      }
    }

Get version for package:

    % curl -v http://127.0.0.1:8000/djdi/versions/packages/Django/
    ...
    < HTTP/1.0 200 OK
    < Content-Type: application/vnd.api+json
    ...
    {
      "data": {
        "category": "packages",
        "version": "1.7.5",
        "name": "Django"
      },
      "links": {
        "self": "/djdi/versions/packages/Django/"
      }
    }

Specified package not found:

    % curl -v http://127.0.0.1:8000/djdi/versions/packages/awesomepackage/
    ...
    < HTTP/1.0 404 NOT FOUND
    < Content-Type: text/html; charset=utf-8
    ...


# License

*django-debug-informer* is licensed under the MIT license. See the license file for details.
