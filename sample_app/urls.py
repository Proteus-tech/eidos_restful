# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from sample_app.form_views import SampleView, NoPostFormView, NoFormView, ExtraContextView, FormTemplateView

urlpatterns = patterns('',
    url(r'^$', SampleView.as_view()),
    url(r'^/no_post_form_view$', NoPostFormView.as_view()),
    url(r'^/no_form_view$', NoFormView.as_view()),
    url(r'^/extra_context_view$', ExtraContextView.as_view()),
    url(r'^/form_template_view$', FormTemplateView.as_view())
)

from sample_app.instance_views import SampleInstanceView

urlpatterns += patterns('',
    url(r'^/instance/(?P<id>\d+)$', SampleInstanceView.as_view())
)