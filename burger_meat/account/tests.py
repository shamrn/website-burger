from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

class TestRegister(TestCase):
    def setUp(self) -> None:
        self.client = Client()


    def test_register(self):
        pass