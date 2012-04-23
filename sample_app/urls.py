# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from sample_app.views import SampleView

urlpatterns = patterns('',
    url(r'^$', SampleView.as_view()),
)