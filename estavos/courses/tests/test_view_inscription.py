from django.core.urlresolvers import reverse
from django.test import TestCase
from estavos.courses.forms import InscriptionForm


class InscriptionsGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('courses:inscription'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/inscription.html')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, InscriptionForm)