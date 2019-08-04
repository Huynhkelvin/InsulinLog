from django.test import SimpleTestCase
from django.urls import reverse, resolve
from logs.views import insulinform, detail, display

class TestsUrls(SimpleTestCase):

        def test_logs_url_is_resolves(self):
            url = reverse('logs')
            self.assertEquals(resolve(url).func,insulinform)

        def test_display_url_is_resolves(self):
            url = reverse('display')
            self.assertEquals(resolve(url).func,display)

        def test_detail_url_is_resolves(self):
            url = reverse('detail')
            self.assertEquals(resolve(url).func,detail)
