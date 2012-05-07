# -*- coding: utf-8 -*-

from django.test import TestCase

from sample_app.models import SampleModel

class TestSampleInstanceView(TestCase):
    def setUp(self):
        self.instance = SampleModel.objects.create(a_field='abcd')

    def test_get_existing_instance_200(self):
        response = self.client.get('/sample_app/instance/%s' % self.instance.id)
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_instance_404(self):
        response = self.client.get('/sample_app/instance/%s' % (self.instance.id+1))
        self.assertEqual(response.status_code, 404)

    def test_put_existing_instance_200(self):
        response = self.client.put('/sample_app/instance/%s' % self.instance.id, {'a_field': 'def'})
        self.assertEqual(response.status_code, 200)

        # need to re-get to get the new value
        updated_instance = SampleModel.objects.get(id=self.instance.id)
        self.assertEqual(updated_instance.a_field, 'def')

    def test_put_non_existing_instance_404(self):
        response = self.client.put('/sample_app/instance/%s' % (self.instance.id+1), {'a_field': 'def'})
        self.assertEqual(response.status_code, 404)

    def test_delete_existing_instance_204(self):
        response = self.client.delete('/sample_app/instance/%s' % self.instance.id)
        self.assertEqual(response.status_code, 204)

    def test_delete_non_existing_instance_404(self):
        response = self.client.delete('/sample_app/instance/%s' % (self.instance.id+1))
        self.assertEqual(response.status_code, 404)

    def test_delete_then_get_410(self):
        self.test_delete_existing_instance_204()
        response = self.client.get('/sample_app/instance/%s' % self.instance.id)
        self.assertEqual(response.status_code, 410)

    def test_delete_then_put_410(self):
        self.test_delete_existing_instance_204()
        response = self.client.put('/sample_app/instance/%s' % self.instance.id)
        self.assertEqual(response.status_code, 410)

    def test_delete_then_delete_410(self):
        self.test_delete_existing_instance_204()
        response = self.client.delete('/sample_app/instance/%s' % self.instance.id)
        self.assertEqual(response.status_code, 410)


