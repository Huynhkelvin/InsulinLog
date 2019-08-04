from django.test import TestCase, Client
from django.urls import reverse
from food.models import Foodinfo, Foodtype

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.calccarb_url = reverse('calccarb')
        self.addfooditem_url = reverse('addfooditem')

    def test_calccarb_GET(self):
        response = self.client.get(self.calccarb_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'food/carbcount.html')

    def test_addfooditem_GET(self):
        response = self.client.get(self.addfooditem_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'food/addfood.html')
