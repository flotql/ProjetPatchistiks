from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import *

### FUNCTIONS ###

def create_user(username,email,password):
    return User.objects.create_user(username,email,password)


### TEST MODELS ###
class TestModelHome(TestCase):

    def test_home_display(self):
        """
        Test if home page is displayed (code 200 = request succes)
        """
        response = self.client.get(reverse('patchistiks:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_button_not_log(self):
        response = self.client.get(reverse('patchistiks:home'))
        self.assertContains(response, "Login")
        self.assertContains(response, "Register")
        self.assertNotContains(response, "Profile")

    def test_home_button_log(self):
        user = create_user("test","test","test")
        url = reverse('patchistiks:home')
        self.client.login(username="test", password="test")
        response = self.client.get(url)
        self.assertContains(response, "Profile")
        self.assertContains(response, "Logout")
        self.assertNotContains(response, "Register")

