# -*- coding: utf-8 -*-

from djangorestframework.resources import Resource

from sample_app.models import SampleModel

class SampleResource(Resource):
    model = SampleModel