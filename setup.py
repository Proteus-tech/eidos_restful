#!/usr/bin/env python

from distutils.core import setup

setup(
    name='restful',
    version='1.2.2',
    description='RESTful for Django',
    author='Proteus Technologies',
    author_email='team@proteus-tech.com',
    url='http://proteus-tech.com',
    # django is Eidos current version of django
    install_requires=['django==1.3.1', 'djangorestframework>=0.3.3', 'django-serene>=0.0.5', 'django-piston==0.2.3'],
    dependency_links = ['git+git://github.com/scoursen/django-softdelete.git@b8f11f7bd3bf68c3b3c961833a91017ca6a4bc56#egg=django-softdelete-0.3.4'],
    package_data={'restful': ['templates/restful/*.html']},
    packages=['restful'],
)