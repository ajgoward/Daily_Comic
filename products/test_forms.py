from django.test import TestCase
from .forms import ReviewForm, ProductForm


class testContactForms(TestCase):

    def test_name_is_required(self):
        form = ReviewForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_rating_is_required(self):
        form = ReviewForm({'rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(
            form.errors['rating'][0], 'This field is required.')

    def test_description_is_required(self):
        form = ReviewForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')


class testProductForms(TestCase):

    def test_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_description_is_required(self):
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_rrp_is_required(self):
        form = ProductForm({'rrp': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rrp', form.errors.keys())
        self.assertEqual(
            form.errors['rrp'][0], 'This field is required.')
