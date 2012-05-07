# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from sample_app.form_views import SampleView, NoPostFormView, NoFormView

urlpatterns = patterns('',
    url(r'^$', SampleView.as_view()),
    url(r'^/no_post_form_view$', NoPostFormView.as_view()),
    url(r'^/no_form_view$', NoFormView.as_view()),
)

from sample_app.instance_views import SampleInstanceView

urlpatterns += patterns('',
    url(r'^/instance/<?id>$', SampleInstanceView.as_view())
)