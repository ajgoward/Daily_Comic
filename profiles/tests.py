from django.test import TestCase


class testContactview(TestCase):

    def shows_correct_product_template(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/theprofile.html')
