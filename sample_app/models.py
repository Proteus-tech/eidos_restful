# -*- coding: utf-8 -*-
from django.db import models

class SampleModel(models.Model):
    a_field = models.CharField(max_length=3)