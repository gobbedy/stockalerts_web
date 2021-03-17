from django.test import TestCase
from django.test import Client
from .views import index, test
from django.urls import resolve
import os

class TemplateTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_templates(self):
        print("Testing Templates")

        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        found = resolve('/test/')
        self.assertEqual(found.func, test)

        unused_dir_relative = 'templates/data_visualization/unused'
        pages = os.listdir(unused_dir_relative)
        for page in pages:
            response = self.client.get('/' + page + '/')
            self.assertEqual(response.status_code, 200)
