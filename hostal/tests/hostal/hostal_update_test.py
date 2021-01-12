from django.test import TestCase
from django.urls import reverse

class HostalUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_hostal_update_page(self):
        response = self.client.get(reverse('hostal_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hostal/hostal_update.html')