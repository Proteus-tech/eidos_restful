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

class ExtraContextResource(Resource):
    model = SampleModel
    post_form = SampleForm
    form_extra_context = {
        'extra': 'extra'
    }

class FormTemplateResource(Resource):
    model = SampleModel
    post_form = SampleForm
    form_template = 'sample_template.html'