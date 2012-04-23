# -*- coding: utf-8 -*-

from restful.drf_views import CreateModelWithFormView

from sample_app.form import SampleForm
from sample_app.resources import SampleResource

class SampleView(CreateModelWithFormView):
    form = SampleForm
    resource = SampleResource

class BadView(CreateModelWithFormView):
    resource = SampleResource