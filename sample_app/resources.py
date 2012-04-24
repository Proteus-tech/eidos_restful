# -*- coding: utf-8 -*-

from djangorestframework.resources import Resource

from sample_app.models import SampleModel
from sample_app.form import SampleForm

class SampleResource(Resource):
    model = SampleModel
    post_form = SampleForm

class NoPostFormResource(Resource):
    model = SampleModel
    form = SampleForm

class NoFormResource(Resource):
    model = SampleModel