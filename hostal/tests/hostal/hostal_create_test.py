from django.test import TestCase
from django.urls import reverse

class HostalCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_hostal_create_page(self):
        response = self.client.get(reverse('hostal_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hostal/hostal_create.html')