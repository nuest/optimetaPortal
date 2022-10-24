import os
import unittest
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optimetaPortal.settings')

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page(self):
        response = self.client.get('/login/')

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.context['publications']), 5)

        self.assertEqual(response.get('Content-Type'), 'text/html; charset=utf-8')

        response = self.client.post('/login/', {'email': 'optimeta@dev.dev'})
        self.assertEqual(response.status_code, 302)
        self.assertRegexpMatches(response.url, 'success')

    @unittest.skip('Login tests need to adjusted for new UI')
    def test_login_page_errors(self):
        response = self.client.put('/login/')
        self.assertEqual(response.status_code, 400)
