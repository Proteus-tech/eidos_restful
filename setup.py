#!/usr/bin/env python

from distutils.core import setup

setup(
    name='restful',
    version='1.2.7',
    description='RESTful for Django',
    author='Proteus Technologies',
    author_email='team@proteus-tech.com',
    url='http://proteus-tech.com',
    # django is Eidos current version of django
    dependency_links = ['http://github.com/scoursen/django-softdelete/tarball/master#egg=django-softdelete-0.3.4',],
    setup_requires = ['django-softdelete==0.3.4'],
    install_requires=['django==1.3.1', 'djangorestframework>=0.3.3', 'django-serene>=0.0.5', 'django-piston==0.2.3'],
    package_data={'restful': ['templates/restful/*.html']},
    packages=['restful'],
)