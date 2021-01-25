from .views import *
from .models import *
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your tests here.

class AuthenticatedTest(APITestCase):
    client_class = APIClient

    def setUp(self):
        self.surname = 'Kozak'
        self.user = User.objects.create_user(surname='Kozak', email='kozak@wp.pl',
                                             password='haslo')
        Token.objects.create(user=self.user)
        super(AuthenticatedTest, self).setUp()
