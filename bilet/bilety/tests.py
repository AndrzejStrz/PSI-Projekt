from . import views
from . import models
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from django import urls
import datetime

# Create your tests here.

class AuthenticatedTest(APITestCase):
    client_class = APIClient

    def setUp(self):
        self.username = 'Kozak'
        self.user = User.objects.create_user(username='Kozak', email='kozak@wp.pl',
                                             password='toniejesthaslo')
        Token.objects.create(user=self.user)
        super(AuthenticatedTest, self).setUp()


class UserTest(AuthenticatedTest):
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

    def test_filter_user(self):

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

        filter_data = {'Name': new_name}
        url = '{0}?{1}'.format(reverse(views.UserList.name), urlencode(filter_data))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Name'] == new_name

    def test_order_User(self):
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

        ordering_address = {'Name': new_name, 'Surname': new_surname}
        url = '{0}?{1}'.format(reverse(views.UserList.name), urlencode(ordering_address))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Name'] == new_name

class TicketOptionTest(AuthenticatedTest):

    def post_ticket(self, price, ticket_name):
        url = reverse(views.Ticket_OptionsList.name)
        data = {'Price': price, 'Ticket_Name': ticket_name}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.post(url, data, format='json', REMOTE_USER=self.username)
        return response

    def test_post_end_ticket_option(self):
        new_price = float(14.5)
        new_ticket_name  = "name"
        response = self.post_ticket(new_price, new_ticket_name)

        assert response.status_code == status.HTTP_201_CREATED
        assert models.Ticket_Options.objects.count() == 1
        assert models.Ticket_Options.objects.get().Price == new_price
        assert models.Ticket_Options.objects.get().Ticket_Name == new_ticket_name

    def test_delete_ticket_option(self):
        new_price = float(14.5)
        new_ticket_name = "name"
        response = self.post_ticket(new_price, new_ticket_name)
        url = urls.reverse(views.Ticket_OptionsDetail.name, None, {response.data['pk']})
        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_update_ticket_option(self):
        new_price = float(14.5)
        new_ticket_name = "name"
        update = 'name1'
        response = self.post_ticket(new_price, new_ticket_name)
        url = urls.reverse(views.Ticket_OptionsDetail.name, None, {response.data['pk']})
        data = {'Ticket_Name': update}
        patch_response = self.client.patch(url, data, format='json')

        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['Ticket_Name'] == update

    def test_search_ticket_option(self):
        new_price = float(14.5)
        new_ticket_name = "name"

        new_price1 = float(15.3)
        new_ticket_name1 = "name1"

        self.post_ticket(new_price, new_ticket_name)
        self.post_ticket(new_price1, new_ticket_name1)

        search_data = {'Price': new_price, 'Ticket_Name': new_ticket_name}
        url = '{0}?{1}'.format(reverse(views.Ticket_OptionsList.name), urlencode(search_data))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Price'] == new_price
        assert response.data['results'][0]['Ticket_Name'] == new_ticket_name

    def test_filter_ticket_option(self):
        new_price = float(14.5)
        new_ticket_name = "name"

        new_price1 = float(15.3)
        new_ticket_name1 = "name1"

        self.post_ticket(new_price, new_ticket_name)
        self.post_ticket(new_price1, new_ticket_name1)

        filter_data = {'Price': new_price , 'Ticket_Name':new_ticket_name}
        url = '{0}?{1}'.format(reverse(views.Ticket_OptionsList.name), urlencode(filter_data))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Price'] == new_price
        assert response.data['results'][0]['Ticket_Name'] == new_ticket_name

    def test_order_ticket_options(self):
        new_price = float(14.5)
        new_ticket_name = "name"

        new_price1 = float(15.3)
        new_ticket_name1 = "name1"

        self.post_ticket(new_price, new_ticket_name)
        self.post_ticket(new_price1, new_ticket_name1)

        ordering_address = {'Price': new_price, 'Ticket': new_ticket_name}
        url = '{0}?{1}'.format(reverse(views.Ticket_OptionsList.name), urlencode(ordering_address))
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Price'] == new_price
        assert response.data['results'][0]['Ticket_Name'] == new_ticket_name