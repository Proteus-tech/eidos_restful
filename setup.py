#!/usr/bin/env python

from distutils.core import setup

setup(name='restful',
      version='1.2',
      description='RESTful for Django',
      author='Proteus Technologies',
      author_email='team@proteus-tech.com',
      url='http://proteus-tech.com',
      install_requires=['django>=1.2', 'djangorestframework>=0.3.3', 'django-serene>=0.0.5', 'django-piston==0.2.3'],
      package_data={'templates': []},
      packages=['restful'],
     )