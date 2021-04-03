from django.urls import reverse
from cart.forms import CartAddProductForm
from django.test import Client, TestCase


class TestCart(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_url(self):
        url = reverse('cart:cart_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_form_not_valid(self):
        form_data = {'quantity': 20}
        form = CartAddProductForm(data=form_data)
        self.assertTrue(form.is_valid())