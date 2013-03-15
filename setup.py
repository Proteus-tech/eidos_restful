#!/usr/bin/env python

from distutils.core import setup

setup(
    name='restful',
    version='1.3.4',
    description='RESTful for Django',
    author='Proteus Technologies',
    author_email='team@proteus-tech.com',
    url='http://proteus-tech.com',
    # django is Eidos current version of django
    install_requires=['django>=1.3.1', 'django-serene>=0.0.5', 'django-piston==0.2.3', 'django-softdelete==0.3.4'],
    package_data={'restful': ['templates/restful/*.html']},
    packages=['restful', 'restful.middleware'],
)