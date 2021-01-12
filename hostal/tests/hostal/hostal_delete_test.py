from django.test import TestCase
from django.urls import reverse

class HostalDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_hostal_delete_page(self):
        response = self.client.get(reverse('hostal_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hostal/hostal_delete.html')