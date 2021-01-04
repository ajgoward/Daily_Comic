from django.test import TestCase


class testCheckoutview(TestCase):

    def shows_correct_template(self):
        response = self.client.get('/checkout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
