from . import views
from .models import *
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from django import urls

# Create your tests here.

class RemoteAuthenticatedTest(APITestCase):
    client_class = APIClient

    def setUp(self):
        self.username = 'mister_neutron'
        self.user = User.objects.create_user(username='mister_neutron', email='mister_neutron@example.com',
                                             password='F4kePaSs0d')
        Token.objects.create(user=self.user)
        super(RemoteAuthenticatedTest, self).setUp()


class UserTest(RemoteAuthenticatedTest):
    def post_user(self, name, surname, login, password, mail):
        url = reverse(views.UserList.name)
        data = {'Name': name, 'Surname': surname, 'Login': login, 'Password': password, 'Mail': mail}
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.user.auth_token.key)
        response = self.client.post(url, data, format='json', REMOTE_USER=self.username)
        return response

    def test_post_end_user(self):

        new_name = 'Name'
        new_surname = 'Surname'
        new_login = 'Login'
        new_password = 'Password'
        new_mail = 'Mail'
        response = self.post_user(new_name, new_surname, new_login, new_password, new_mail)

        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1
        assert User.objects.get().Name == new_name

