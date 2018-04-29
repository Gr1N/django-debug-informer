# README

## About

This sample project demonstrates how to use the debug informer. It is designed
to run under the latest stable version of Django, currently 1.9.x.


## How to

The test project requires a working installation of Django:

    % pip install Django

The following commands must be run from the root directory of a checkout of
the debug informer, ie. the directory that contains ``example/``.

Before running the example for the first time, you must create a database:

    % PYTHONPATH=. django-admin.py migrate --settings=example.settings

Then you can use the following command to run the example:

    % PYTHONPATH=. django-admin.py runserver --settings=example.settings
