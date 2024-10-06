from django.test import TestCase
from .forms import CollaborateForm


# Create your tests here.
class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'mayn',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
    
    def test_name_is_required(self):
        """ Test for name field """
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name is missing")

    def test_email_is_required(self):
        """ Test for email field """
        form = CollaborateForm({
            'name': 'User',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Email is missing")

    def test_message_is_required(self):
        """ Test for message field """
        form = CollaborateForm({
            'name': 'User',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Message is missing")