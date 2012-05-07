# -*- coding: utf-8 -*-
from restful.drf_mixins import InstanceModelWithSoftDeleteView

from sample_app.resources import NoFormResource

class SampleInstanceView(InstanceModelWithSoftDeleteView):
    resource = NoFormResource
