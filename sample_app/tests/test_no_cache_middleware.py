# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpRequest

from django.test import TestCase
from restful.middleware.cache import NoCacheMiddleware

class TestNoCacheMiddleware(TestCase):
    def test_get_response(self):
        response = self.client.get('/sample_app')
        self.assertTrue(response.has_header('Cache-Control'))
        self.assertEqual(response['Cache-Control'], 'no-cache, no-store')

    def test_put_response(self):
        response = self.client.put('/sample_app', data={'a_field': 'abc'})
        self.assertTrue(response.has_header('Cache-Control'))
        self.assertEqual(response['Cache-Control'], 'no-cache, no-store')

    def test_post_request_is_not_set_to_no_cache(self):
        response = self.client.post('/sample_app', data={'a_field': 'abc'})
        self.assertFalse(response.has_header('Cache-Control'))

    def test_put_request_with_response_which_has_cache_control_header_should_not_be_updated(self):
        request = HttpRequest()
        request.method = 'PUT'
        response = HttpResponse()
        response['Cache-Control'] = 'max-age=3600'

        middleware = NoCacheMiddleware()
        updated_response = middleware.process_response(request,response)
        self.assertTrue(updated_response.has_header('Cache-Control'))
        self.assertEqual(updated_response['Cache-Control'], 'max-age=3600')

    def test_get_request_with_response_which_has_cache_control_header_should_not_be_updated(self):
        request = HttpRequest()
        request.method = 'GET'
        response = HttpResponse()
        response['Cache-Control'] = 'max-age=3600'

        middleware = NoCacheMiddleware()
        updated_response = middleware.process_response(request,response)
        self.assertTrue(updated_response.has_header('Cache-Control'))
        self.assertEqual(updated_response['Cache-Control'], 'max-age=3600')
