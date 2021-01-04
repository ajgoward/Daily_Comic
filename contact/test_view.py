from django.test import TestCase


class testContactview(TestCase):

    def shows_correct_template(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contactus.html')
