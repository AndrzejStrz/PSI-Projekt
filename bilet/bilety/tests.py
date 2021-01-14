from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import User
from rest_framework import status
from django.utils.http import urlencode
from django import urls


# Create your tests here.

class UserTests(APITestCase):
    def post_User_test(self, name):
        url = reverse(views.UserList.name)
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

