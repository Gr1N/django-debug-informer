from os import path

from setuptools import (
    find_packages,
    setup,
)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = [l.split('\n')[0] for l in f.readlines()]

setup(
    name='django-debug-informer',
    version='0.4.0',
    description='A simple application that helps you to display various debug information about the Django project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Nikita Grishko',
    author_email='gr1n@protonmail.com',
    url='https://github.com/Gr1N/django-debug-informer',
    packages=find_packages(exclude=(
        'tests.*',
        'tests',
        'example',
    )),
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='django debug',
    project_urls={
        'Bug Reports': 'https://github.com/Gr1N/django-debug-informer/issues',
        'Source': 'https://github.com/Gr1N/django-debug-informer',
    }
)
