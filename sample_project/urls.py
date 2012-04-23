from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^sample_app', include('sample_app.urls')),
)
