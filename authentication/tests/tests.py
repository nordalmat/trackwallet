from django.test import TestCase
from django.urls import reverse

from authentication.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.proper_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password1': 'Password123',
            'password2': 'Password123'
        }
        self.no_username_user = {
            'username': '',
            'email': 'email@gmail.com',
            'password1': 'Password123',
            'password2': 'Password123'
        }
        self.no_email_user = {
            'username': 'username',
            'email': '',
            'password1': 'Password123',
            'password2': 'Password123'
        }
        self.bad_format_email_user = {
            'username': 'username',
            'email': 'email',
            'password1': 'Password123',
            'password2': 'Password123'
        }
        self.username_taken_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password1': 'Password123',
            'password2': 'Password123'
        }
        self.email_taken_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password1': 'Password123',
            'password2': 'Password123'
        }
        self.no_password_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password1': '',
            'password2': ''
        }
        self.no_digit_password_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password1': 'Password',
            'password2': 'Password'
        }
        self.no_uppercase_password_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password1': 'password123',
            'password2': 'password123'
        }
        self.no_lowercase_password_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password1': 'PASSWORD123',
            'password2': 'PASSWORD123'
        }
        self.no_matching_password_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password1': 'Password123',
            'password2': 'Password12'
        }

        return super().setUp()


class RegisterTest(BaseTest):
    def test_user_can_access_registration_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_register_proper_user(self):
        response = self.client.post(self.register_url, self.proper_user, format='text/html')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_register_no_username_user(self):
        try:
            response = self.client.post(self.register_url, self.no_username_user, format='text/html')
        except ValueError:
            pass
        self.assertEqual(User.objects.count(), 0)

    def test_register_no_email_user(self):
        response = self.client.post(self.register_url, self.no_email_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_register_bad_format_email_user(self):
        response = self.client.post(self.register_url, self.bad_format_email_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_username_taken_user(self):
        response = self.client.post(self.register_url, self.proper_user, format='text/html')
        response = self.client.post(self.register_url, self.username_taken_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)

    def test_email_taken_user(self):
        response = self.client.post(self.register_url, self.proper_user, format='text/html')
        response = self.client.post(self.register_url, self.email_taken_user, format='text/html')
        self.assertEqual(User.objects.count(), 1)
    
    def test_no_password_user(self):
        response = self.client.post(self.register_url, self.no_password_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_no_digit_password_user(self):
        response = self.client.post(self.register_url, self.no_digit_password_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_no_uppercase_password_user(self):
        response = self.client.post(self.register_url, self.no_uppercase_password_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_no_lowercase_password_user(self):
        response = self.client.post(self.register_url, self.no_lowercase_password_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_no_matching_password_user(self):
        response = self.client.post(self.register_url, self.no_matching_password_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)
