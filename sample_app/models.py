# -*- coding: utf-8 -*-
from django.db import models
from softdelete.models import SoftDeleteObject

class SampleModel(SoftDeleteObject):
    a_field = models.CharField(max_length=3)