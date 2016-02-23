# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.courses.forms import InscriptionForm
from estavos.courses.models import Inscription, Course


class InscriptionGet(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 03, 12),
            classes='Crianças',
            is_active=True
        )
        self.resp = self.client.get(r('courses:inscription', self.course.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/inscription_form.html')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, InscriptionForm)

    def test_context(self):
        """course instance should exists in context"""
        course = self.resp.context['course']
        self.assertIsInstance(course, Course)


class InscriptionGetInvalid(TestCase):
    def setUp(self):
        self.obj = Course.objects.create(
            name='Curso APRENDA #2',
            place='Núcleo de Xadrez do clube ASCADE',
            start_date=date(2016, 02, 20),
            classes='Crianças, Adultos',
            is_active=False
        )
        self.resp = self.client.get(r('courses:inscription', self.obj.pk))

    def test_inactive_course_should_redirect_to_courses_list(self):
        self.assertEqual(302, self.resp.status_code)

    def test_redirect(self):
        """inactive course should redirects to courses list page"""
        self.assertRedirects(self.resp, r('courses:list'))



class InscriptionPostValid(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 03, 12),
            classes='Crianças',
            is_active=True
        )
        data = dict(name='Bruno Barbosa', phone='(61) 2222-2222', email='bsbruno1@gmail.com',
                    student='Ana Beatriz', birth='01/09/2009')
        self.resp = self.client.post(r('courses:inscription', self.course.pk), data)

    def test_post(self):
        """Valid POST should redirect to thanks page"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_inscription_mail(self):
        self.assertEqual(2, len(mail.outbox))

    def test_save_inscription(self):
        self.assertTrue(Inscription.objects.exists())


class InscriptionPostInvalid(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 03, 12),
            classes='Crianças',
            is_active=True
        )
        self.resp = self.client.post(r('courses:inscription', self.course.pk), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_not_save_inscription(self):
        self.assertFalse(Inscription.objects.exists())