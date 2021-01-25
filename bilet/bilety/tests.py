from . import views
from . import models
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
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
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
        assert models.User.objects.count() == 1
        assert models.User.objects.get().Name == new_name
        assert models.User.objects.get().Surname == new_surname
        assert models.User.objects.get().Login == new_login
        assert models.User.objects.get().Password == new_password
        assert models.User.objects.get().Mail == new_mail

    def test_delete_user(self):

        new_name = 'Name'
        new_surname = 'Surname'
        new_login = 'Login'
        new_password = 'Password'
        new_mail = 'Mail'
        response = self.post_user(new_name, new_surname, new_login, new_password, new_mail)
        url = urls.reverse(views.UserDetail.name, None, {response.data['pk']})
        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_update_user(self):

        new_name = 'Name'
        new_surname = 'Surname'
        new_login = 'Login'
        new_password = 'Password'
        new_mail = 'Mail'
        update = 'new mail'
        response = self.post_user(new_name, new_surname, new_login, new_password, new_mail)
        url = urls.reverse(views.UserDetail.name, None, {response.data['pk']})
        data = {'Mail': update}
        patch_response = self.client.patch(url, data, format='json')

        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['Mail'] == update

    def test_search_user(self):

        new_name = 'Name'
        new_surname = 'Surname'
        new_login = 'Login'
        new_password = 'Password'
        new_mail = 'Mail'

        new_name1 = 'Name1'
        new_surname1 = 'Surname1'
        new_login1 = 'Login1'
        new_password1 = 'Password1'
        new_mail1 = 'Mail1'

        self.post_user(new_name, new_surname, new_login, new_password, new_mail)
        self.post_user(new_name1, new_surname1, new_login1, new_password1, new_mail1)

        search_data = {'Name': new_name, 'Surname': new_surname}
        url = '{0}?{1}'.format(reverse(views.UserList.name), urlencode(search_data))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Name'] == new_name
        assert response.data['results'][0]['Surname'] == new_surname

