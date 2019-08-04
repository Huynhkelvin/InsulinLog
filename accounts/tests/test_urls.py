from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import home, signup, log_in, logout_view

class TestsUrls(SimpleTestCase):

        def test_signup_url_is_resolves(self):
            url = reverse('signup')
            self.assertEquals(resolve(url).func,signup)

        def test_login_url_is_resolves(self):
            url = reverse('login')
            self.assertEquals(resolve(url).func,log_in)

        def test_logout_url_is_resolves(self):
            url = reverse('logout')
            self.assertEquals(resolve(url).func,logout_view)

        def test_home_url_is_resolves(self):
            url = reverse('home')
            self.assertEquals(resolve(url).func,home)
