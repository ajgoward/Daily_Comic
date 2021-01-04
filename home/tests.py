from django.test import TestCase


class testHomeview(TestCase):

    def shows_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
