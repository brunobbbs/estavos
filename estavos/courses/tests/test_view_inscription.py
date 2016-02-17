import unittest

from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.courses.forms import InscriptionForm


class InscriptionsGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('courses:inscription'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/inscription_form.html')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, InscriptionForm)


class InscriptionPostValid(TestCase):
    def setUp(self):
        # ['name', 'phone', 'email', 'place', 'klass', 'student', 'birth']
        data = dict(name='Bruno Barbosa', phone='(61) 8121-7870', email='bsbruno1@gmail.com', place='ascade',
                    klass='adults', student='Ana Beatriz', birth='2009-09-01')
        self.resp = self.client.post(r('courses:inscription'), data)

    def test_post(self):
        """Valid POST should redirect to thanks page"""
        self.assertRedirects(self.resp, r('courses:thanks'))


    def test_send_inscription_mail(self):
        self.assertEqual(1, len(mail.outbox))


class InscriptionPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('courses:inscription'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)