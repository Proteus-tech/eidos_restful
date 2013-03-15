# -*- coding: utf-8 -*-

from django.test import TestCase

class TestSampleView(TestCase):
    def test_get_view(self):
        response = self.client.get('/sample_app')
        self.assertContains(response, '<input id="id_a_field" type="text" name="a_field" maxlength="3" />')

    def test_post_view(self):
        response = self.client.post('/sample_app', data={'a_field': 'abc'})
        self.assertContains(response, 'abc', status_code=201)

class TestNoPostFormView(TestCase):
    def test_get_view(self):
        response = self.client.get('/sample_app/no_post_form_view')
        self.assertContains(response, u'The server did not implement this view correct.', status_code=500)

class TestNoFormView(TestCase):
    def test_get_view(self):
        response = self.client.get('/sample_app/no_form_view')
        self.assertContains(response, u'The server did not implement this view correct.', status_code=500)

class TestExtraContextView(TestCase):
    def test_get_view(self):
        response = self.client.get('/sample_app/extra_context_view')
        print response.content
        self.assertEquals(response.context['extra'], 'extra')
