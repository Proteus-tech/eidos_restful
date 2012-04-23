# -*- coding: utf-8 -*-

from restful.drf_views import CreateModelWithFormView

from sample_app.form import SampleForm

class SampleView(CreateModelWithFormView):
    form = SampleForm