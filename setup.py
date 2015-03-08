# -*- coding: utf-8 -*-

from io import open
from setuptools import setup, find_packages


setup(
    name='django-debug-informer',
    version='0.1.0',
    description='A simple application that helps displays various debug information about the Django project',
    long_description=open('README.md', encoding='utf-8').read(),
    author='Nikita Grishko',
    author_email='grin.minsk+github@gmail.com',
    url='https://github.com/Gr1N/django-debug-informer',
    download_url='https://pypi.python.org/pypi/django-debug-informer',
    license='MIT',
    packages=find_packages(exclude=(
        'tests.*',
        'tests',
        'example',
    )),
    install_requires=(
        'django>=1.4.2',
    ),
    extras_require={
        'test': (
            'tox',
        ),
        'development': (
            'flake8',
            'zest.releaser',
            'check-manifest',
            'coverage',
        ),
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
