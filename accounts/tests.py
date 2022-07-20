from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'username': 'test_username',
            'email': 'test_email@gmail.com',
            'password': 'test_password5!',
            'first_name': 'User',
            'last_name': 'Zuckerberg'
        }
        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_access_apge(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_can_register(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)


class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
