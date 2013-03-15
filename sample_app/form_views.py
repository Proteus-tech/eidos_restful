# -*- coding: utf-8 -*-

from restful.drf_views import CreateModelWithFormView

from sample_app.resources import SampleResource, NoPostFormResource, NoFormResource, ExtraContextResource, \
    FormTemplateResource


class SampleView(CreateModelWithFormView):
    resource = SampleResource

class NoPostFormView(CreateModelWithFormView):
    resource = NoPostFormResource

class NoFormView(CreateModelWithFormView):
    resource = NoFormResource

class ExtraContextView(CreateModelWithFormView):
    resource = ExtraContextResource

class FormTemplateView(CreateModelWithFormView):
    resource = FormTemplateResource