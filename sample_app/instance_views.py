# -*- coding: utf-8 -*-

from serene.views import InstanceModelView
from restful.drf_mixins import SoftDeleteReadModelMixin

from sample_app.resources import NoFormResource

class SampleInstanceView(SoftDeleteReadModelMixin, InstanceModelView):
    resource = NoFormResource
