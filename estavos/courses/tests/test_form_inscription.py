from django.test import TestCase
from estavos.courses.forms import InscriptionForm


class InscriptionFormTest(TestCase):
    def setUp(self):
        self.form = InscriptionForm()

    def test_form_has_fields(self):
        expected = ['name', 'phone', 'email', 'place', 'klass', 'student', 'birth']
        self.assertSequenceEqual(expected, list(self.form.fields))