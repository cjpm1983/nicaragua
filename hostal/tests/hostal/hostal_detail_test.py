from django.test import TestCase
from django.urls import reverse

class HostalDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_hostal_detail_page(self):
        response = self.client.get(reverse('hostal_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hostal/hostal_detail.html')