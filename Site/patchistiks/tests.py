from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import *


# Create your tests here.
class ViewTest(TestCase):

    def test_home_display(self):
        """
        Test if home page is displayed (code 200 = request succes)
        """
        response = self.client.get(reverse('patchistiks:home'))
        self.assertEqual(response.status_code, 200)

