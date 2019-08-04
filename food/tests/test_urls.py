from django.test import SimpleTestCase
from django.urls import reverse, resolve
from food.views import calculatecarb, addfood

class TestsUrls(SimpleTestCase):

        def test_calccarb_url_is_resolves(self):
            url = reverse('calccarb')
            self.assertEquals(resolve(url).func,calculatecarb)

        def test_addfooditem_url_is_resolves(self):
            url = reverse('addfooditem')
            self.assertEquals(resolve(url).func,addfood)
