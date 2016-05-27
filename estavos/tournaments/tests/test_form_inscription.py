from django.test import TestCase
from estavos.tournaments.forms import InscriptionForm


class InscriptionFormTest(TestCase):

    def setUp(self):
        self.form = InscriptionForm()

    def test_form_has_fields(self):
        """Form must have four fields"""
        expected = ['name', 'email', 'birth', 'id_cbx', 'id_fide', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))