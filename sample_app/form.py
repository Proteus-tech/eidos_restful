# -*- coding: utf-8 -*-

from django import forms

from sample_app.models import SampleModel

class SampleForm(forms.ModelForm):
    class Meta:
        model = SampleModel