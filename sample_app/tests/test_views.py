# -*- coding: utf-8 -*-

from django.test import TestCase

class TestSampleView(TestCase):
    def test_get_view(self):
        response = self.client.get('/sample_app')
        self.assertEqual(response.status_code, 200)