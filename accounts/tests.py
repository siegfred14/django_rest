from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework import status

# Create your tests here.


class UserTest(APITestCase):

    def setUp(self):
        self.test_user = User.objects.create_user('example', 'example@gmail.com', 'passexample')
        self.create_url = reverse('account-create')

    def test_create_user(self):

        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)