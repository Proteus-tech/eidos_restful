# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from sample_app.views import SampleView, BadView

urlpatterns = patterns('',
    url(r'^$', SampleView.as_view()),
    url(r'^/bad_view', BadView.as_view()),
)