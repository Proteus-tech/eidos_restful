# -*- coding: utf-8 -*-

from django.test import TestCase

class TestNoCacheMiddleware(TestCase):
    def test_get_response(self):
        response = self.client.get('/sample_app')
        self.assertTrue(response.has_header('Cache-Control'))
        self.assertEqual(response['Cache-Control'], 'no-cache, no-store')

    def test_put_response(self):
        response = self.client.put('/sample_app', data={'a_field': 'abc'})
        self.assertTrue(response.has_header('Cache-Control'))
        self.assertEqual(response['Cache-Control'], 'no-cache, no-store')
