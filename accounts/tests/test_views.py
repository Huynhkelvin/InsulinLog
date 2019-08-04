from django.test import TestCase, Client
from django.urls import reverse
from patient.models import Patient
from logs.models import DailyInsulin
from django.contrib.auth.models import User



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('logout')
        self.login_url = reverse('login')
        self.signup_url = reverse('signup')
        self.home_url = reverse('home')
        self.user = User.objects.create_user(username='testuser', password='insulinlog')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code,302)

    def test_log_in_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/login.html')

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/signup.html')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/home.html')
