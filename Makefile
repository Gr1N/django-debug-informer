.PHONY: example test flake8 coverage

example:
	PYTHONPATH=. \
		django-admin.py migrate --settings=example.settings
	PYTHONPATH=. \
		django-admin.py runserver --settings=example.settings

test:
	DJANGO_SETTINGS_MODULE=tests.settings \
		django-admin.py test tests

flake8:
	flake8 debug_informer example tests

coverage:
	coverage erase
	DJANGO_SETTINGS_MODULE=tests.settings \
		coverage run --branch --source=debug_informer `which django-admin.py` test tests
	coverage html
